
import pandas as pd
import matplotlib.pyplot as mp
#walter_meas



def plot_all(Device_name,device_number,W,L,SETUP_linear_1,SETUP_linear_2,VB_Bias,VD_linear,path_assessment_curves,path_point_meas,filename,point_data_flname):

#    Device_name="ESDNMOS"

    walter_meas_path= r"C:\\All_projects\tc18d_model_assessment\Data\correct\ESDNMOS\\"

#    path_assessment_curves= r"C:\All_projects\tc18d_model_assessment\Data\ESD_data_Wafer14_repeatability\Assessment_curves\\"

#    filename='ESDNMOS_025.clr'





    #read text file into pandas DataFrame



    with open( path_assessment_curves + filename) as f:

        df = pd.read_csv(f, sep="\t",header=None)
        df2=df.dropna()
 #       print(df)
 #       print(len(df2))




    df.columns = ["W", "L", "VB", "VG", "VD", "ID", "IB", "TEMP", "SETUP", "NF", "SA","EMPTY"]


 #   print(df)






    #werner_meas_path_clear= r"C:\All_projects\tc18d_model_assessment\Data\ESD_data_Wafer14_repeatability\ESDNMOS\\"

    #flname = "M018xW6C442W14x025xESDNMOSx0{:01d}x".format(site+1)+"TP25.txt"

    #point_data_flname = "M018xW6C442W14x025xESDNMOSx" + device_number + "xxTP25_clr.txt"


    with open( path_point_meas + point_data_flname) as f:
        ff = pd.read_csv(f, delim_whitespace=True,header=None)
        ff2=ff.dropna()
  #      print(ff)
  #      print(len(ff))

    #SIT DNO REP  SU        W        L  NF  TMP           VG        VBULK           VD           VS        VSMU5           IG        IBULK           ID           IS        ISMU5

    ff.columns = ["SIT", "DNO", "REP", "SU", "W", "L", "NF", "TMP", "VG", "VBULK", "VD","VS","VSMU5","IG","IBULK","ID","IS","ISMU5"]

 #   print(ff)

    ff_id_vg_1 = ff[(ff['W'] == W) & (ff['L'] == L) & (ff['VD'] == VD_linear) & (ff['VG'] > 0.9)]

 #   print(ff_id_vg_1)


    ff_id_vg_1.plot(x="VG", y=["ID"],linewidth=1.0, linestyle="",marker="^", color="red" )

    #mp.show()




    fig, ax = mp.subplots()
    df_id_vg_1 = df[(df['W'] == W) & (df['L'] == L) & (df['SETUP'] == SETUP_linear_1) & (df['VB'] == VB_Bias)]

    print(df_id_vg_1)

    #df_id_vg_1.plot(x="VG", y=["ID"],linewidth=1.0, linestyle="",marker="." )

    #mp.show()



    df_id_vg_2 = df[(df['W'] == W) & (df['L'] == L) & (df['SETUP'] == SETUP_linear_2) & (df['VB'] == VB_Bias)]

 #   print(df_id_vg_2)

    #df_id_vg_2.plot(x="VG", y=["ID"],linewidth=1.0, linestyle="",marker="." )

    #mp.show()


    for df in [df_id_vg_1, df_id_vg_2]:
        mp.plot(df['VG'], df['ID'])

    ff_id_vg_1.plot(x="VG", y=["ID"],linewidth=1.0, linestyle="",marker="^", color="red",ax=ax )

    mp.legend(['ID-Sweep1','ID-Sweep2','point-measurements-12'])


    if VD_linear==0.1:
        picname = Device_name + "_" +device_number + "_W=" + str(W)+ "_L=" + str(L) + "_Linear_xTP25.png"
        mp.title(picname)

        mp.savefig(picname)
        mp.grid()
        mp.show()

    else:
        picname = Device_name + "_" + device_number + "_W=" + str(W) + "_L=" + str(L) + "_Saturation_xTP25.png"
        mp.title(picname)
        mp.savefig(picname)
        mp.grid()
        mp.show()



