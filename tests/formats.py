import sys
import os
from pandas import DataFrame, Series
sys.path.insert(0, os.path.abspath("../"))
import yagamee
from yagamee.formats import FormatFunction

result = DataFrame(columns=["e","f","g","E","G","F"])
for d in map(str, range(1, 6)):
    e_format: FormatFunction = yagamee.formats.create_e_format(d)
    f_format: FormatFunction = yagamee.formats.create_f_format(d)
    g_format: FormatFunction = yagamee.formats.create_g_format(d)
    translated_e_format: FormatFunction = yagamee.formats.create_translated_e_format(
        d)
    translated_g_format: FormatFunction = yagamee.formats.create_translated_g_format(
        d)
    force_f_format:FormatFunction=yagamee.formats.create_force_f_format(d)
    for x in [1234*10**(-i) for i in range(1, 8)]:
        series = Series({
            "e": e_format(x),
            "f": f_format(x),
            "g": g_format(x),
            "E": translated_e_format(x),
            "G": translated_g_format(x),
            "F": force_f_format(x)
        })
        result.loc[f"{x},{d}"] = series
print(result)
yagamee.dataframe_tools.preview_in_excel(result)