# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_docs.ipynb.

# %% ../nbs/00_docs.ipynb 3
from __future__ import annotations
from .import_essentials import *
import nbdev
from fastcore.basics import AttrDict
from fastcore.utils import *

from nbdev.showdoc import *
from nbdev.doclinks import *
from inspect import isclass
from nbdev.showdoc import (
    _ext_link, 
    _wrap_sig, 
    _fmt_anno, 
    _f_name, 
    DocmentTbl, 
    _maybe_nm, 
    _show_param
)
from nbdev.config import get_config

# %% auto 0
__all__ = ['CalloutDocument', 'CustomizedMarkdownRenderer']

# %% ../nbs/00_docs.ipynb 4
def _docment_parser(parser: BaseParser):
    p = parser.schema()['properties']
    anno = parser.__annotations__
    d = { 
        k: {
            'anno': anno[k],
            'default': v['default'] if 'default' in v else inspect._empty,
            'docment': v['description'] if 'description' in v else inspect._empty,
        } for k, v in p.items()
    }

    d = AttrDict(d)
    return d


# %% ../nbs/00_docs.ipynb 5
class ParserMarkdownRenderer(BasicMarkdownRenderer):
    def __init__(self, sym, name: str | None = None, title_level: int = 3):
        super().__init__(sym, name, title_level)
        self.dm.dm = _docment_parser(sym)

# %% ../nbs/00_docs.ipynb 6
def _italic(s: str): return f'*{s}*' if s.strip() else s

def _bold(s: str): return f'**{s}**' if s.strip() else s

# %% ../nbs/00_docs.ipynb 7
def _show_param(param):
    "Like `Parameter.__str__` except removes: quotes in annos, spaces, ids in reprs"
    kind,res,anno,default = param.kind,param._name,param._annotation,param._default
    kind = '*' if kind==inspect._VAR_POSITIONAL else '**' if kind==inspect._VAR_KEYWORD else ''
    res = kind+res
    # if anno is not inspect._empty: res += f':{_f_name(anno) or _fmt_anno(anno)}'
    if default is not inspect._empty: res += f'={_f_name(default) or repr(default)}'
    return res


def _fmt_sig(sig):
    if sig is None: return ''
    p = {k:v for k,v in sig.parameters.items()}
    _params = [_show_param(p[k]) for k in p.keys() if k != 'self']
    return "(" + ', '.join(_params)  + ")"


# %% ../nbs/00_docs.ipynb 8
def _inner_list2mdlist(l: list):
    param_name, param_anno, param_default, param_doc = l
    # annotation
    if param_anno == inspect._empty: param_anno = None
    else: param_anno = f"`{param_anno}`"
    # default value
    if param_default == inspect._empty: param_default = None
    else: param_default = f"*default={param_default}*"

    mdoc = ""
    if param_anno and param_default:
        mdoc += f"* {_bold(param_name)} ({param_anno}, {param_default})"
    elif param_anno:
        mdoc += f"* {_bold(param_name)} ({param_anno})"
    elif param_default:
        mdoc += f"* {_bold(param_name)} ({param_default})"
    else:
        mdoc += f"* {_bold(param_name)}"
    
    if not (param_doc == inspect._empty): 
        mdoc += f" -- {param_doc}"
    return mdoc

def _params_mdlist(tbl: DocmentTbl):
    param_list = [
        L([k, v['anno'], v['default'], v['docment']])
        for k, v in tbl.dm.items() if k != 'return'
    ]
    # param_list = tbl._row_list
    return L(param_list).map(_inner_list2mdlist)

def _return_mdlist(tbl: DocmentTbl):
    return_list = [tbl.dm['return'][k] for k in ['anno', 'default', 'docment']]
    param_anno, param_default, param_doc = return_list
    mdoc = ""
    if not param_anno == inspect._empty: 
        mdoc += f"(`{param_anno}`)"
    if param_doc != inspect._empty:
        mdoc += f" -- {param_doc}"
    return mdoc

def _show_params_return(tbl: DocmentTbl):
    if not tbl.has_docment: return ''
    doc = "" 
    doc = "::: {#docs .callout-note icon=false}\n\n"
    doc += '## Parameters:' + '\n'
    doc += _params_mdlist(tbl)
    doc += "\n\n:::\n\n"
    if tbl.has_return:
        doc += "::: {#docs .callout-note icon=false}\n\n"
        doc += '\n\n## Returns:\n'
        doc += f"&ensp;&ensp;&ensp;&ensp;{_return_mdlist(tbl)}"
        doc += "\n\n:::"
    
    return '\n'.join(doc)

# %% ../nbs/00_docs.ipynb 9
class CalloutDocument():
    def __init__(self, tbl: DocmentTbl):
        self.tbl = tbl
    
    def _repre_mardown(self):
        return _show_params_return(self.tbl)

    __str__ = _repre_mardown

# %% ../nbs/00_docs.ipynb 10
class CustomizedMarkdownRenderer(ShowDocRenderer):
    def __init__(self, sym, name:str|None=None, title_level:int=3):
        super().__init__(sym, name, title_level)
        self.isclass = inspect.isclass(sym)

    def _repr_markdown_(self):
        doc = '---\n\n'
        # doc = ''
        src = NbdevLookup().code(self.fn)
        _look_up = NbdevLookup()[self.fn]
        if _look_up: 
            module_dir = _look_up[1].replace('.py', '').replace('/', '.') + '.'
        else:
            module_dir = None
        
        if src: 
            link = _ext_link(src, 'source', 'style="float:right; font-size:smaller"') + '\n\n'
        else:
            link = ''
        h = '#'*self.title_level
        doc += f'{h} {str(self.nm).upper()} {link}\n\n'
        # if self.isclass: doc += '> *class* '
        # else: doc += '> '
        if self.isclass: doc += '::: {.doc-sig}\n\n CLASS '
        else: doc += '::: {.doc-sig}\n\n '
        sig = f"{module_dir}{_bold(self.nm)} *{_fmt_sig(self.sig)}*\n\n:::"
        doc += f'{sig}'
        if self.docs: doc += f"\n\n{self.docs}"
        # if self.dm.has_docment: doc += f"\n\n{_show_params_return(self.dm)}"
        if self.dm.has_docment: doc += f"\n\n{CalloutDocument(self.dm)}"

        return doc

    # __repr__=_repr_markdown_

