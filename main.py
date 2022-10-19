
import pandas as pd
import matplotlib.pyplot as mp
#walter_meas

Device_name="ESDNMOS"

walter_meas_path= r"C:\\All_projects\tc18d_model_assessment\Data\correct\ESDNMOS\\"

werner_repeat_meas= r"C:\All_projects\tc18d_model_assessment\Data\ESD_data_Wafer14_repeatability\Assessment_curves\\"

filename='ESDNMOS_025.clr'





#read text file into pandas DataFrame



with open( werner_repeat_meas + filename) as f:

    df = pd.read_csv(f, sep="\t")
    df2=df.dropna()
    print(df)
    print(len(df2))




df.columns = ["W", "L", "VB", "VG", "VD", "ID", "IB", "TEMP", "SETUP", "NF", "SA","EMPTY"]


print(df)






werner_meas_path_clear= r"C:\All_projects\tc18d_model_assessment\Data\ESD_data_Wafer14_repeatability\ESDNMOS\\"

#flname = "M018xW6C442W14x025xESDNMOSx0{:01d}x".format(site+1)+"TP25.txt"

flname = "M018xW6C442W14x025xESDNMOSx01xxTP25_clr.txt"


with open( werner_meas_path_clear + flname) as f:
    ff = pd.read_csv(f, delim_whitespace=True)
    ff2=ff.dropna()
    print(ff)
    print(len(ff))

#SIT DNO REP  SU        W        L  NF  TMP           VG        VBULK           VD           VS        VSMU5           IG        IBULK           ID           IS        ISMU5

ff.columns = ["SIT", "DNO", "REP", "SU", "W", "L", "NF", "TMP", "VG", "VBULK", "VD","VS","VSMU5","IG","IBULK","ID","IS","ISMU5"]

print(ff)

ff_id_vg_1 = ff[(ff['W'] == 0.000032) & (ff['L'] == 3.6e-7) & (ff['VD'] == 0.1) & (ff['VG'] > 0.9)]

print(ff_id_vg_1)


ff_id_vg_1.plot(x="VG", y=["ID"],linewidth=1.0, linestyle="",marker="^", color="red" )

#mp.show()




fig, ax = mp.subplots()
df_id_vg_1 = df[(df['W'] == 0.000032) & (df['L'] == 3.6e-7) & (df['SETUP'] == 1) & (df['VB'] == 0)]

print(df_id_vg_1)

#df_id_vg_1.plot(x="VG", y=["ID"],linewidth=1.0, linestyle="",marker="." )

#mp.show()



df_id_vg_2 = df[(df['W'] == 0.000032) & (df['L'] == 3.6e-7) & (df['SETUP'] == 6) & (df['VB'] == 0)]

print(df_id_vg_2)

#df_id_vg_2.plot(x="VG", y=["ID"],linewidth=1.0, linestyle="",marker="." )

#mp.show()


for df in [df_id_vg_1, df_id_vg_2]:
    mp.plot(df['VG'], df['ID'])

ff_id_vg_1.plot(x="VG", y=["ID"],linewidth=1.0, linestyle="",marker="^", color="red",ax=ax )

mp.legend(['ID-Sweep1','ID-Sweep2','point-measurements-12'])


picname = Device_name + "_01xTP25.png"
mp.title(picname)






mp.savefig(picname)
mp.grid()
mp.show()
