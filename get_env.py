from utils import format_markdown_table


env_var_vals = ['', 'False', '0', '1234', '12234.5']
columns = [''] + map(repr, env_var_vals)
rows = []
for target_type in [bool, int, float, str]:
    row = ['**%s()**' % target_type.__name__]
    for env_var_val in env_var_vals:
        try:
            res = repr(target_type(env_var_val))
        except Exception as ex:
            res = type(ex).__name__
        row.append(res)
    rows.append(row)

print format_markdown_table(rows, columns)
