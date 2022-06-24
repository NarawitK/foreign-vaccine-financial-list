from dataaccess.dbconnector import MariaDBConnector
from dataaccess.hosxp_dataaccess import HosxpDataAccess
from spreadsheet_modules.resolver import Resolver

# Testing Backend
# TO-DO: GUI
if __name__ == "__main__":
    resolver = Resolver()
    dbaccess_instance = HosxpDataAccess(MariaDBConnector().get_instance())
    list_res = dbaccess_instance.query_injection_by_visitdate('2021-11-01', '2022-01-15')
    resolver.convert_hosxp_to_df(list_res)
    res_frame = resolver.merge_dataframes(resolver.hosxp_df, resolver.mophic_df)
    resolver.export_to_excel("D:/Users/PC220321/Desktop/dataframe_result.xlsx", res_frame)
