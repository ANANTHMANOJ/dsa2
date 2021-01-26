import pandas as pd
import json


def generate_colgroup(path_input ,path_output):
  df = pd.read_csv(path_input)
  colid = ""
  colcat, colnum, coltext = [], [], []
  coly = ""
  Num = ['int','int32','int64','float','float32','float64']
  df_size = len(df)
  for cols in df.columns:
    print(cols)
    if cols != coly:
      col_size = df[cols].unique().size
      if col_size == df_size and colid == "":
        colid = str(cols)
        df[cols] = df[cols].astype(df[cols].dtype)
      elif df[cols].dtype in Num:
        colnum.append(cols)
        df[cols] =df[cols].astype(df[cols].dtype)
      elif col_size > (df_size/2):
        coltext.append(cols)
        df[cols] = df[cols].astype(str)
      else:
        colcat.append(cols)
        df[cols] = df[cols].astype('category')
  ddict = {
    'colid' : colid,
    'colnum' : colnum,
    'colcat' : colcat,
    'coltext' : coltext
  }
  print('ddict' ,ddict)
  out_file = open(path_output+'cols_group.json','w')
  json.dump(ddict,out_file)


if __name__ == "__main__":
    import fire
    fire.Fire()

