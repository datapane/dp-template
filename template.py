import datapane as dp

# Build report
v = dp.Blocks("Datapane template")
dp.save_report(v, path="template.html", open=True)