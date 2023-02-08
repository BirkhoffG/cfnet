# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/04_learning.ipynb.

# %% ../nbs/04_learning.ipynb 3
from __future__ import annotations
from .import_essentials import *
from .data import TabularDataModule
from .module import BaseTrainingModule
from .logger import TensorboardLogger
from .utils import validate_configs
from ._ckpt_manager import CheckpointManager

# %% auto 0
__all__ = ['TrainingConfigs', 'train_model_with_states', 'train_model']

# %% ../nbs/04_learning.ipynb 4
class TrainingConfigs(BaseParser):
    """Configurator of `train_model`."""
    
    n_epochs: int = Field(
        description="Number of epochs."
    )
    batch_size: int = Field(
        description="Batch size."
    )
    monitor_metrics: Optional[str] = Field(
        None, description="Monitor metrics used to evaluate the training result after each epoch."
    )
    seed: int = Field(
        42, description="Seed for generating random number."
    )
    log_dir: str = Field(
        "log", description="The name for the directory that holds logged data during training."
    )
    logger_name: str = Field(
        "debug", description="The name for the directory that holds logged data during training under log directory."
    )
    log_on_step: bool = Field(
        False, description="Log the evaluate metrics at the current step."
    )
    max_n_checkpoints: int = Field(
        3, description="Maximum number of checkpoints stored."
    )

    @property
    def PRNGSequence(self):
        return hk.PRNGSequence(self.seed)


# %% ../nbs/04_learning.ipynb 5
def train_model_with_states(
    training_module: BaseTrainingModule,
    params: hk.Params,
    opt_state: optax.OptState,
    data_module: TabularDataModule,
    t_configs: Dict[str, Any] | TrainingConfigs,
) -> Tuple[hk.Params, optax.OptState]:
    """Train models with `params` and `opt_state`."""

    t_configs = validate_configs(t_configs, TrainingConfigs)
    keys = t_configs.PRNGSequence
    # define logger
    logger = TensorboardLogger(
        log_dir=t_configs.log_dir,
        name=t_configs.logger_name,
        on_step=t_configs.log_on_step,
    )
    logger.save_hyperparams(t_configs.dict())
    if training_module.hparams:
        logger.save_hyperparams(training_module.hparams)

    training_module.init_logger(logger)
    # define checkpoint manageer
    if t_configs.monitor_metrics is None:
        monitor_metrics = None
    else:
        monitor_metrics = f"{t_configs.monitor_metrics}_epoch"

    ckpt_manager = CheckpointManager(
        log_dir=Path(training_module.logger.log_dir) / "checkpoints",
        monitor_metrics=monitor_metrics,
        max_n_checkpoints=t_configs.max_n_checkpoints,
    )
    # dataloaders
    train_loader = data_module.train_dataloader(t_configs.batch_size)
    val_loader = data_module.val_dataloader(t_configs.batch_size)

    # start training
    for epoch in range(t_configs.n_epochs):
        training_module.logger.on_epoch_started()
        # training
        with tqdm(
            train_loader, unit="batch", leave=epoch == t_configs.n_epochs - 1
        ) as t_loader:
            t_loader.set_description(f"Epoch {epoch}")
            for batch in t_loader:
                x, y = map(device_put, tuple(batch))
                params, opt_state = training_module.training_step(
                    params, opt_state, next(keys), (x, y)
                )
                # logs = training_module.training_step_logs(
                #     params, next(keys), (x, y))
                logs = training_module.logger.get_last_logs()
                t_loader.set_postfix(**logs)
                # logger.log(logs)

        # validation
        for batch in val_loader:
            x, y = map(device_put, tuple(batch))
            logs = training_module.validation_step(params, next(keys), (x, y))
            # logger.log(logs)
        epoch_logs = training_module.logger.on_epoch_finished()
        ckpt_manager.update_checkpoints(params, opt_state, epoch_logs, epoch)

    training_module.logger.close()
    return params, opt_state


# %% ../nbs/04_learning.ipynb 6
def train_model(
    training_module: BaseTrainingModule, # Training module
    data_module: TabularDataModule, # Data module
    t_configs: Dict[str, Any] | TrainingConfigs, # Training configurator
) -> Tuple[hk.Params, optax.OptState]:
    """Train models."""
    
    t_configs = validate_configs(t_configs, TrainingConfigs)
    keys = t_configs.PRNGSequence 
    params, opt_state = training_module.init_net_opt(data_module, next(keys))
    return train_model_with_states(
        training_module=training_module,
        params=params,
        opt_state=opt_state,
        data_module=data_module,
        t_configs=t_configs,
    )
