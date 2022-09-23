# Autogenerated by nbdev

d = { 'settings': { 'branch': 'master',
                'doc_baseurl': '/cfnet/',
                'doc_host': 'https://birkhoffg.github.io',
                'git_url': 'https://github.com/birkhoffg/cfnet/tree/master/',
                'lib_path': 'cfnet'},
  'syms': { 'cfnet.datasets': { 'cfnet.datasets.DataModuleConfigs': ('datasets.html#datamoduleconfigs', 'cfnet/datasets.py'),
                                'cfnet.datasets.NumpyDataset': ('datasets.html#numpydataset', 'cfnet/datasets.py'),
                                'cfnet.datasets.NumpyDataset.__getitem__': ('datasets.html#numpydataset.__getitem__', 'cfnet/datasets.py'),
                                'cfnet.datasets.NumpyDataset.__init__': ('datasets.html#numpydataset.__init__', 'cfnet/datasets.py'),
                                'cfnet.datasets.NumpyDataset.__len__': ('datasets.html#numpydataset.__len__', 'cfnet/datasets.py'),
                                'cfnet.datasets.NumpyLoader': ('datasets.html#numpyloader', 'cfnet/datasets.py'),
                                'cfnet.datasets.NumpyLoader.__init__': ('datasets.html#numpyloader.__init__', 'cfnet/datasets.py'),
                                'cfnet.datasets.TabularDataModule': ('datasets.html#tabulardatamodule', 'cfnet/datasets.py'),
                                'cfnet.datasets.TabularDataModule.__init__': ( 'datasets.html#tabulardatamodule.__init__',
                                                                               'cfnet/datasets.py'),
                                'cfnet.datasets.TabularDataModule._update_configs': ( 'datasets.html#tabulardatamodule._update_configs',
                                                                                      'cfnet/datasets.py'),
                                'cfnet.datasets.TabularDataModule.check_cols': ( 'datasets.html#tabulardatamodule.check_cols',
                                                                                 'cfnet/datasets.py'),
                                'cfnet.datasets.TabularDataModule.get_sample_X': ( 'datasets.html#tabulardatamodule.get_sample_x',
                                                                                   'cfnet/datasets.py'),
                                'cfnet.datasets.TabularDataModule.prepare_data': ( 'datasets.html#tabulardatamodule.prepare_data',
                                                                                   'cfnet/datasets.py'),
                                'cfnet.datasets.TabularDataModule.test_dataloader': ( 'datasets.html#tabulardatamodule.test_dataloader',
                                                                                      'cfnet/datasets.py'),
                                'cfnet.datasets.TabularDataModule.train_dataloader': ( 'datasets.html#tabulardatamodule.train_dataloader',
                                                                                       'cfnet/datasets.py'),
                                'cfnet.datasets.TabularDataModule.val_dataloader': ( 'datasets.html#tabulardatamodule.val_dataloader',
                                                                                     'cfnet/datasets.py'),
                                'cfnet.datasets._numpy_collate': ('datasets.html#_numpy_collate', 'cfnet/datasets.py'),
                                'cfnet.datasets.find_imutable_idx_list': ('datasets.html#find_imutable_idx_list', 'cfnet/datasets.py')},
            'cfnet.evaluate': { 'cfnet.evaluate.CFExplanationResults': ('evaluate.html#cfexplanationresults', 'cfnet/evaluate.py'),
                                'cfnet.evaluate.CFExplanationResults.__post_init__': ( 'evaluate.html#cfexplanationresults.__post_init__',
                                                                                       'cfnet/evaluate.py'),
                                'cfnet.evaluate._create_second_order_cfs': ('evaluate.html#_create_second_order_cfs', 'cfnet/evaluate.py'),
                                'cfnet.evaluate.benchmark_cfs': ('evaluate.html#benchmark_cfs', 'cfnet/evaluate.py'),
                                'cfnet.evaluate.compute_manifold_dist': ('evaluate.html#compute_manifold_dist', 'cfnet/evaluate.py'),
                                'cfnet.evaluate.compute_predictive_acc': ('evaluate.html#compute_predictive_acc', 'cfnet/evaluate.py'),
                                'cfnet.evaluate.compute_proximity': ('evaluate.html#compute_proximity', 'cfnet/evaluate.py'),
                                'cfnet.evaluate.compute_so_proximity': ('evaluate.html#compute_so_proximity', 'cfnet/evaluate.py'),
                                'cfnet.evaluate.compute_so_sparsity': ('evaluate.html#compute_so_sparsity', 'cfnet/evaluate.py'),
                                'cfnet.evaluate.compute_so_validity': ('evaluate.html#compute_so_validity', 'cfnet/evaluate.py'),
                                'cfnet.evaluate.compute_sparsity': ('evaluate.html#compute_sparsity', 'cfnet/evaluate.py'),
                                'cfnet.evaluate.compute_validity': ('evaluate.html#compute_validity', 'cfnet/evaluate.py'),
                                'cfnet.evaluate.evaluate_cfs': ('evaluate.html#evaluate_cfs', 'cfnet/evaluate.py'),
                                'cfnet.evaluate.generate_cf_results': ('evaluate.html#generate_cf_results', 'cfnet/evaluate.py'),
                                'cfnet.evaluate.generate_cf_results_cfnet': ( 'evaluate.html#generate_cf_results_cfnet',
                                                                              'cfnet/evaluate.py'),
                                'cfnet.evaluate.generate_cf_results_local_exp': ( 'evaluate.html#generate_cf_results_local_exp',
                                                                                  'cfnet/evaluate.py'),
                                'cfnet.evaluate.get_runtime': ('evaluate.html#get_runtime', 'cfnet/evaluate.py')},
            'cfnet.import_essentials': {},
            'cfnet.interfaces': { 'cfnet.interfaces.BaseCFExplanationModule': ( 'inferfaces.html#basecfexplanationmodule',
                                                                                'cfnet/interfaces.py'),
                                  'cfnet.interfaces.BaseCFExplanationModule.generate_cfs': ( 'inferfaces.html#basecfexplanationmodule.generate_cfs',
                                                                                             'cfnet/interfaces.py'),
                                  'cfnet.interfaces.BaseCFExplanationModule.name': ( 'inferfaces.html#basecfexplanationmodule.name',
                                                                                     'cfnet/interfaces.py'),
                                  'cfnet.interfaces.BaseCFExplanationModule.update_cat_info': ( 'inferfaces.html#basecfexplanationmodule.update_cat_info',
                                                                                                'cfnet/interfaces.py'),
                                  'cfnet.interfaces.LocalCFExplanationModule': ( 'inferfaces.html#localcfexplanationmodule',
                                                                                 'cfnet/interfaces.py')},
            'cfnet.logger': { 'cfnet.logger.TensorboardLogger': ('logger.html#tensorboardlogger', 'cfnet/logger.py'),
                              'cfnet.logger.TensorboardLogger.__init__': ('logger.html#tensorboardlogger.__init__', 'cfnet/logger.py'),
                              'cfnet.logger.TensorboardLogger.close': ('logger.html#tensorboardlogger.close', 'cfnet/logger.py'),
                              'cfnet.logger.TensorboardLogger.get_last_logs': ( 'logger.html#tensorboardlogger.get_last_logs',
                                                                                'cfnet/logger.py'),
                              'cfnet.logger.TensorboardLogger.log': ('logger.html#tensorboardlogger.log', 'cfnet/logger.py'),
                              'cfnet.logger.TensorboardLogger.log_dict': ('logger.html#tensorboardlogger.log_dict', 'cfnet/logger.py'),
                              'cfnet.logger.TensorboardLogger.log_dir': ('logger.html#tensorboardlogger.log_dir', 'cfnet/logger.py'),
                              'cfnet.logger.TensorboardLogger.on_epoch_finished': ( 'logger.html#tensorboardlogger.on_epoch_finished',
                                                                                    'cfnet/logger.py'),
                              'cfnet.logger.TensorboardLogger.on_epoch_started': ( 'logger.html#tensorboardlogger.on_epoch_started',
                                                                                   'cfnet/logger.py'),
                              'cfnet.logger.TensorboardLogger.save_hyperparams': ( 'logger.html#tensorboardlogger.save_hyperparams',
                                                                                   'cfnet/logger.py')},
            'cfnet.methods.diverse': { 'cfnet.methods.diverse.DiverseCF': ('methods.diverse.html#diversecf', 'cfnet/methods/diverse.py'),
                                       'cfnet.methods.diverse.DiverseCF.__init__': ( 'methods.diverse.html#diversecf.__init__',
                                                                                     'cfnet/methods/diverse.py'),
                                       'cfnet.methods.diverse.DiverseCF.generate_cf': ( 'methods.diverse.html#diversecf.generate_cf',
                                                                                        'cfnet/methods/diverse.py'),
                                       'cfnet.methods.diverse.DiverseCF.generate_cfs': ( 'methods.diverse.html#diversecf.generate_cfs',
                                                                                         'cfnet/methods/diverse.py'),
                                       'cfnet.methods.diverse.DiverseCFConfig': ( 'methods.diverse.html#diversecfconfig',
                                                                                  'cfnet/methods/diverse.py'),
                                       'cfnet.methods.diverse.DiverseCFConfig.keys': ( 'methods.diverse.html#diversecfconfig.keys',
                                                                                       'cfnet/methods/diverse.py'),
                                       'cfnet.methods.diverse._compute_regularization_loss': ( 'methods.diverse.html#_compute_regularization_loss',
                                                                                               'cfnet/methods/diverse.py'),
                                       'cfnet.methods.diverse._diverse_cf': ( 'methods.diverse.html#_diverse_cf',
                                                                              'cfnet/methods/diverse.py'),
                                       'cfnet.methods.diverse.dpp_style': ('methods.diverse.html#dpp_style', 'cfnet/methods/diverse.py'),
                                       'cfnet.methods.diverse.hinge_loss': ('methods.diverse.html#hinge_loss', 'cfnet/methods/diverse.py'),
                                       'cfnet.methods.diverse.l1_mean': ('methods.diverse.html#l1_mean', 'cfnet/methods/diverse.py')},
            'cfnet.methods.proto': { 'cfnet.methods.proto.AE': ('methods.prototype.html#ae', 'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.AE.__call__': ('methods.prototype.html#ae.__call__', 'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.AE.__init__': ('methods.prototype.html#ae.__init__', 'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.AEConfigs': ('methods.prototype.html#aeconfigs', 'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.AETrainingModule': ( 'methods.prototype.html#aetrainingmodule',
                                                                               'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.AETrainingModule.__init__': ( 'methods.prototype.html#aetrainingmodule.__init__',
                                                                                        'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.AETrainingModule._training_step': ( 'methods.prototype.html#aetrainingmodule._training_step',
                                                                                              'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.AETrainingModule.encode': ( 'methods.prototype.html#aetrainingmodule.encode',
                                                                                      'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.AETrainingModule.forward': ( 'methods.prototype.html#aetrainingmodule.forward',
                                                                                       'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.AETrainingModule.init_net_opt': ( 'methods.prototype.html#aetrainingmodule.init_net_opt',
                                                                                            'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.AETrainingModule.loss_fn': ( 'methods.prototype.html#aetrainingmodule.loss_fn',
                                                                                       'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.AETrainingModule.training_step': ( 'methods.prototype.html#aetrainingmodule.training_step',
                                                                                             'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.AETrainingModule.validation_step': ( 'methods.prototype.html#aetrainingmodule.validation_step',
                                                                                               'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.ProtoCF': ('methods.prototype.html#protocf', 'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.ProtoCF.__init__': ( 'methods.prototype.html#protocf.__init__',
                                                                               'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.ProtoCF.generate_cf': ( 'methods.prototype.html#protocf.generate_cf',
                                                                                  'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.ProtoCF.generate_cfs': ( 'methods.prototype.html#protocf.generate_cfs',
                                                                                   'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.ProtoCF.update_cat_info': ( 'methods.prototype.html#protocf.update_cat_info',
                                                                                      'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto.ProtoCFConfig': ( 'methods.prototype.html#protocfconfig',
                                                                            'cfnet/methods/proto.py'),
                                     'cfnet.methods.proto._proto_cf': ('methods.prototype.html#_proto_cf', 'cfnet/methods/proto.py')},
            'cfnet.methods.vae_cf': { 'cfnet.methods.vae_cf.Decoder': ('methods.vaecf.html#decoder', 'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.Decoder.__call__': ( 'methods.vaecf.html#decoder.__call__',
                                                                                 'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.Decoder.__init__': ( 'methods.vaecf.html#decoder.__init__',
                                                                                 'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.Encoder': ('methods.vaecf.html#encoder', 'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.Encoder.__call__': ( 'methods.vaecf.html#encoder.__call__',
                                                                                 'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.VAECFConfigs': ('methods.vaecf.html#vaecfconfigs', 'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.VAE_CF': ('methods.vaecf.html#vae_cf', 'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.VAE_CF.__init__': ( 'methods.vaecf.html#vae_cf.__init__',
                                                                                'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.VAE_CF._training_step': ( 'methods.vaecf.html#vae_cf._training_step',
                                                                                      'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.VAE_CF.compute_loss': ( 'methods.vaecf.html#vae_cf.compute_loss',
                                                                                    'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.VAE_CF.forward': ( 'methods.vaecf.html#vae_cf.forward',
                                                                               'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.VAE_CF.generate_cfs': ( 'methods.vaecf.html#vae_cf.generate_cfs',
                                                                                    'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.VAE_CF.init_net_opt': ( 'methods.vaecf.html#vae_cf.init_net_opt',
                                                                                    'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.VAE_CF.loss_fn': ( 'methods.vaecf.html#vae_cf.loss_fn',
                                                                               'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.VAE_CF.predict': ( 'methods.vaecf.html#vae_cf.predict',
                                                                               'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.VAE_CF.training_step': ( 'methods.vaecf.html#vae_cf.training_step',
                                                                                     'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.VAE_CF.validation_step': ( 'methods.vaecf.html#vae_cf.validation_step',
                                                                                       'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.VariationalAutoEncoder': ( 'methods.vaecf.html#variationalautoencoder',
                                                                                       'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.VariationalAutoEncoder.__call__': ( 'methods.vaecf.html#variationalautoencoder.__call__',
                                                                                                'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.VariationalAutoEncoder.__init__': ( 'methods.vaecf.html#variationalautoencoder.__init__',
                                                                                                'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.VariationalAutoEncoder.sample_latent': ( 'methods.vaecf.html#variationalautoencoder.sample_latent',
                                                                                                     'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.init_net_opt_vae': ( 'methods.vaecf.html#init_net_opt_vae',
                                                                                 'cfnet/methods/vae_cf.py'),
                                      'cfnet.methods.vae_cf.make_vae': ('methods.vaecf.html#make_vae', 'cfnet/methods/vae_cf.py')},
            'cfnet.methods.vanilla': { 'cfnet.methods.vanilla.VanillaCF': ('methods.vanilla.html#vanillacf', 'cfnet/methods/vanilla.py'),
                                       'cfnet.methods.vanilla.VanillaCF.__init__': ( 'methods.vanilla.html#vanillacf.__init__',
                                                                                     'cfnet/methods/vanilla.py'),
                                       'cfnet.methods.vanilla.VanillaCF.generate_cf': ( 'methods.vanilla.html#vanillacf.generate_cf',
                                                                                        'cfnet/methods/vanilla.py'),
                                       'cfnet.methods.vanilla.VanillaCF.generate_cfs': ( 'methods.vanilla.html#vanillacf.generate_cfs',
                                                                                         'cfnet/methods/vanilla.py'),
                                       'cfnet.methods.vanilla.VanillaCFConfig': ( 'methods.vanilla.html#vanillacfconfig',
                                                                                  'cfnet/methods/vanilla.py'),
                                       'cfnet.methods.vanilla._vanilla_cf': ( 'methods.vanilla.html#_vanilla_cf',
                                                                              'cfnet/methods/vanilla.py')},
            'cfnet.nets': { 'cfnet.nets.CounterNetModel': ('nets.html#counternetmodel', 'cfnet/nets.py'),
                            'cfnet.nets.CounterNetModel.__call__': ('nets.html#counternetmodel.__call__', 'cfnet/nets.py'),
                            'cfnet.nets.CounterNetModel.__init__': ('nets.html#counternetmodel.__init__', 'cfnet/nets.py'),
                            'cfnet.nets.CounterNetModelConfigs': ('nets.html#counternetmodelconfigs', 'cfnet/nets.py'),
                            'cfnet.nets.DenseBlock': ('nets.html#denseblock', 'cfnet/nets.py'),
                            'cfnet.nets.DenseBlock.__call__': ('nets.html#denseblock.__call__', 'cfnet/nets.py'),
                            'cfnet.nets.DenseBlock.__init__': ('nets.html#denseblock.__init__', 'cfnet/nets.py'),
                            'cfnet.nets.MLP': ('nets.html#mlp', 'cfnet/nets.py'),
                            'cfnet.nets.MLP.__call__': ('nets.html#mlp.__call__', 'cfnet/nets.py'),
                            'cfnet.nets.MLP.__init__': ('nets.html#mlp.__init__', 'cfnet/nets.py'),
                            'cfnet.nets.PredictiveModel': ('nets.html#predictivemodel', 'cfnet/nets.py'),
                            'cfnet.nets.PredictiveModel.__call__': ('nets.html#predictivemodel.__call__', 'cfnet/nets.py'),
                            'cfnet.nets.PredictiveModel.__init__': ('nets.html#predictivemodel.__init__', 'cfnet/nets.py'),
                            'cfnet.nets.PredictiveModelConfigs': ('nets.html#predictivemodelconfigs', 'cfnet/nets.py')},
            'cfnet.train': { 'cfnet.train.TrainingConfigs': ('learning.html#trainingconfigs', 'cfnet/train.py'),
                             'cfnet.train.TrainingConfigs.PRNGSequence': ('learning.html#trainingconfigs.prngsequence', 'cfnet/train.py'),
                             'cfnet.train.train_model': ('learning.html#train_model', 'cfnet/train.py'),
                             'cfnet.train.train_model_with_states': ('learning.html#train_model_with_states', 'cfnet/train.py')},
            'cfnet.training_module': { 'cfnet.training_module.BaseTrainingModule': ( 'training_module.html#basetrainingmodule',
                                                                                     'cfnet/training_module.py'),
                                       'cfnet.training_module.BaseTrainingModule.init_logger': ( 'training_module.html#basetrainingmodule.init_logger',
                                                                                                 'cfnet/training_module.py'),
                                       'cfnet.training_module.BaseTrainingModule.init_net_opt': ( 'training_module.html#basetrainingmodule.init_net_opt',
                                                                                                  'cfnet/training_module.py'),
                                       'cfnet.training_module.BaseTrainingModule.log': ( 'training_module.html#basetrainingmodule.log',
                                                                                         'cfnet/training_module.py'),
                                       'cfnet.training_module.BaseTrainingModule.log_dict': ( 'training_module.html#basetrainingmodule.log_dict',
                                                                                              'cfnet/training_module.py'),
                                       'cfnet.training_module.BaseTrainingModule.save_hyperparameters': ( 'training_module.html#basetrainingmodule.save_hyperparameters',
                                                                                                          'cfnet/training_module.py'),
                                       'cfnet.training_module.BaseTrainingModule.training_step': ( 'training_module.html#basetrainingmodule.training_step',
                                                                                                   'cfnet/training_module.py'),
                                       'cfnet.training_module.BaseTrainingModule.validation_step': ( 'training_module.html#basetrainingmodule.validation_step',
                                                                                                     'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModule': ( 'training_module.html#counternettrainingmodule',
                                                                                           'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModule.__init__': ( 'training_module.html#counternettrainingmodule.__init__',
                                                                                                    'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModule._explainer_step': ( 'training_module.html#counternettrainingmodule._explainer_step',
                                                                                                           'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModule._predictor_step': ( 'training_module.html#counternettrainingmodule._predictor_step',
                                                                                                           'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModule._training_step': ( 'training_module.html#counternettrainingmodule._training_step',
                                                                                                          'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModule._training_step_logs': ( 'training_module.html#counternettrainingmodule._training_step_logs',
                                                                                                               'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModule.exp_loss_fn': ( 'training_module.html#counternettrainingmodule.exp_loss_fn',
                                                                                                       'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModule.forward': ( 'training_module.html#counternettrainingmodule.forward',
                                                                                                   'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModule.generate_cfs': ( 'training_module.html#counternettrainingmodule.generate_cfs',
                                                                                                        'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModule.init_net_opt': ( 'training_module.html#counternettrainingmodule.init_net_opt',
                                                                                                        'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModule.loss_fn_1': ( 'training_module.html#counternettrainingmodule.loss_fn_1',
                                                                                                     'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModule.loss_fn_2': ( 'training_module.html#counternettrainingmodule.loss_fn_2',
                                                                                                     'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModule.loss_fn_3': ( 'training_module.html#counternettrainingmodule.loss_fn_3',
                                                                                                     'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModule.pred_loss_fn': ( 'training_module.html#counternettrainingmodule.pred_loss_fn',
                                                                                                        'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModule.predict': ( 'training_module.html#counternettrainingmodule.predict',
                                                                                                   'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModule.training_step': ( 'training_module.html#counternettrainingmodule.training_step',
                                                                                                         'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModule.validation_step': ( 'training_module.html#counternettrainingmodule.validation_step',
                                                                                                           'cfnet/training_module.py'),
                                       'cfnet.training_module.CounterNetTrainingModuleConfigs': ( 'training_module.html#counternettrainingmoduleconfigs',
                                                                                                  'cfnet/training_module.py'),
                                       'cfnet.training_module.PredictiveTrainingModule': ( 'training_module.html#predictivetrainingmodule',
                                                                                           'cfnet/training_module.py'),
                                       'cfnet.training_module.PredictiveTrainingModule.__init__': ( 'training_module.html#predictivetrainingmodule.__init__',
                                                                                                    'cfnet/training_module.py'),
                                       'cfnet.training_module.PredictiveTrainingModule._training_step': ( 'training_module.html#predictivetrainingmodule._training_step',
                                                                                                          'cfnet/training_module.py'),
                                       'cfnet.training_module.PredictiveTrainingModule.forward': ( 'training_module.html#predictivetrainingmodule.forward',
                                                                                                   'cfnet/training_module.py'),
                                       'cfnet.training_module.PredictiveTrainingModule.init_net_opt': ( 'training_module.html#predictivetrainingmodule.init_net_opt',
                                                                                                        'cfnet/training_module.py'),
                                       'cfnet.training_module.PredictiveTrainingModule.loss_fn': ( 'training_module.html#predictivetrainingmodule.loss_fn',
                                                                                                   'cfnet/training_module.py'),
                                       'cfnet.training_module.PredictiveTrainingModule.training_step': ( 'training_module.html#predictivetrainingmodule.training_step',
                                                                                                         'cfnet/training_module.py'),
                                       'cfnet.training_module.PredictiveTrainingModule.validation_step': ( 'training_module.html#predictivetrainingmodule.validation_step',
                                                                                                           'cfnet/training_module.py'),
                                       'cfnet.training_module.PredictiveTrainingModuleConfigs': ( 'training_module.html#predictivetrainingmoduleconfigs',
                                                                                                  'cfnet/training_module.py'),
                                       'cfnet.training_module.partition_trainable_params': ( 'training_module.html#partition_trainable_params',
                                                                                             'cfnet/training_module.py'),
                                       'cfnet.training_module.project_immutable_features': ( 'training_module.html#project_immutable_features',
                                                                                             'cfnet/training_module.py')},
            'cfnet.utils': { 'cfnet.utils.accuracy': ('utils.html#accuracy', 'cfnet/utils.py'),
                             'cfnet.utils.add_to_class': ('utils.html#add_to_class', 'cfnet/utils.py'),
                             'cfnet.utils.binary_cross_entropy': ('utils.html#binary_cross_entropy', 'cfnet/utils.py'),
                             'cfnet.utils.cat_normalize': ('utils.html#cat_normalize', 'cfnet/utils.py'),
                             'cfnet.utils.check_cat_info': ('utils.html#check_cat_info', 'cfnet/utils.py'),
                             'cfnet.utils.dist': ('utils.html#dist', 'cfnet/utils.py'),
                             'cfnet.utils.grad_update': ('utils.html#grad_update', 'cfnet/utils.py'),
                             'cfnet.utils.init_net_opt': ('utils.html#init_net_opt', 'cfnet/utils.py'),
                             'cfnet.utils.load_json': ('utils.html#load_json', 'cfnet/utils.py'),
                             'cfnet.utils.make_model': ('utils.html#make_model', 'cfnet/utils.py'),
                             'cfnet.utils.proximity': ('utils.html#proximity', 'cfnet/utils.py'),
                             'cfnet.utils.sigmoid': ('utils.html#sigmoid', 'cfnet/utils.py'),
                             'cfnet.utils.validate_configs': ('utils.html#validate_configs', 'cfnet/utils.py')}}}