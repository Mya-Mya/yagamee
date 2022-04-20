from typing import Callable, List, Optional, Dict, Collection, Any
from pandas import DataFrame
from pandas.io import clipboard
from pandas.io.formats.style import Styler
import sigfig
import re
import tempfile
import os
from pathlib import Path

DictData = Dict[str, Collection[Any]]
ListishData = Collection[Any]
def to_dataframe(data:DataFrame|DictData|ListishData|Styler)->DataFrame:
    if(isinstance(data, DataFrame)):
        pass
    elif(isinstance(data, Styler)):
        data = data.data
    else:
        data = DataFrame(data)
    return data

DataFrameOrStyler = DataFrame|Styler
def to_styler(table:DataFrameOrStyler)->Styler:
    if(isinstance(table, DataFrame)):
        table = table.style
    else:
        pass
    return table

sigfig_notation_regex: re.Pattern = re.compile(r"f\d+|g\d+|e\d+|G\d+|\s")
Format=Callable[[float|int],str]
def create_f_formatter(digits: str) -> Format:
    return lambda x: ("{:."+str(digits)+"f}").format(x)
def create_g_formatter(digits: str) -> Format:
    return lambda x: ("{:."+str(digits)+"g}").format(x)
def create_e_formatter(digits: str) -> Format:
    return lambda x: ("{:."+str(digits)+"e}").format(x)
def create_G_formatter(digits: str) -> Format:
    return lambda x:sigfig.round(str(x), sigfigs=int(digits))
Formatter=Dict[str,Format]

def create_formatter(notation: Optional[str],columns:List[str])->Optional[Formatter]:
    if notation is None:
        return None
    formatter: Dict = {}
    notation = notation or ""
    format_order_s = sigfig_notation_regex.findall(notation)
    for format_order, column_name in zip(format_order_s, list(columns)):
        format_method: str = format_order[0]
        format_param: str = format_order[1:]
        format: Format = None
        if(format_method == "f"):
            format = create_f_formatter(format_param)
        elif(format_method == "g"):
            format = create_g_formatter(format_param)
        elif(format_method == "e"):
            format = create_e_formatter(format_param)
        elif(format_method == "G"):
            format = create_G_formatter(format_param)
        if format:
            formatter[column_name] = format
    return formatter

def format_sigfig(table: DataFrameOrStyler, notation: Optional[str]) -> Styler:
    formatter:Optional[Formatter] = create_formatter(notation,table.columns)
    if formatter:
        table:DataFrame = to_dataframe(table).copy()
        for column_name,format in formatter.items():
            table[column_name] = table[column_name].transform(format)
    styler = to_styler(table)
    return styler


def copy_as_latex(
    table: DataFrame,
    sigfig_notation: Optional[str] = None,
    show_index: bool = False,
) -> Styler:
    styler: Styler = format_sigfig(table, sigfig_notation)
    if not show_index:
        styler = styler.hide()
    latex: str = styler.to_latex()
    clipboard.copy(latex)
    return styler

excel_file_path:str = str(Path(tempfile.gettempdir()) / "yagamee_temp_table.xlsx")

def preview_in_excel(
    table: DataFrameOrStyler,
    sigfig_notation: Optional[str] = None
) -> None:
    styler: Styler = format_sigfig(table, sigfig_notation)
    styler.to_excel(excel_file_path)
    os.startfile(excel_file_path)
