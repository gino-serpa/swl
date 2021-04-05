import pathlib
import pandas as pd
import chardet
import csv

def ingest_scielo_folder( data_folder = pathlib.Path.cwd()/'data', encoding='unknown' ):
    '''
    Ingests the scielo files in data_folder and returns a single dataframe
    with all the records

    Input:
        data_folder: Folder containing all the data files.
                     Defaults to 'data' in the current working directory
    Returns:
        df: Pandas dataframe with all the records
    '''

    # Check if folder exist and if there is data in the folder
    if not data_folder.exists():
        print(f'Data folder {str(data_folder)} does not exist!')
        return

    df_list = []
    file_list = sorted(data_folder.glob('*.txt'))
    print('Data Folder exists: ',len(file_list),' files')
    for data_file in file_list:
        print('* Ingesting file: ',data_file)
        if encoding == 'unknown':
            print('Encoding unknown. Checking Encoding')
            rawdata = open (data_file,"rb").read()
            encoding = chardet.detect(rawdata)['encoding']
            print('Encoding: ', encoding)
        df_list.append(ingest_scielo_file(data_file, encoding))

    df = pd.concat(df_list)

    return df

def ingest_scielo_file(file_name, encoding):
    '''
    Ingest an individual data file with data from scielo
        Input:
            file_name: valid name of the file to be ingested
            encoding: file encoding

        Returns:
            df: pandas data frame with the data in the ingested file
    '''
    #print('Ingesting individual file: ',file_name)
    df = pd.read_csv(file_name,
                     encoding=encoding,
                     index_col=False,
                     error_bad_lines=False,
                     quoting = csv.QUOTE_NONE,
                     sep='\t')
    columns={'PT':'publication type',
         'AU': 'authors',
         'BE': 'editors',
         'TI': 'title',
         'X1': 'spanish title',
         'Y1': 'portuguese title',
         'Z1': 'other language title',
         'SO': 'source',
         'LA': 'language',
         'DT': 'document type',
         'DE': 'english author keywords',
         'X5': 'spanish author Keywords',
         'Y5': 'portuguese author keywords',
         'Z5': 'other language author keywords',
         'AB': 'abstract',
         'X4': 'spanish abstract',
         'Y4': 'portuguese abstract',
         'Z4': 'other language abstract',
         'C1': 'addresses',
         'EM': 'emails ',
         'RI': 'research id number',
         'OI': 'orchid id',
         'CR': 'cited references',
         'NR': 'cited references count',
         'TC': 'scielo citation index times cited count',
         'Z9': 'total times cited count',
         'U1': 'usage count 180',
         'U2': 'usage count 2013',
         'PU': 'publisher',
         'PI': 'publisher city',
         'PA': 'publisher address',
         'SN': 'issn',
         'PD': 'pub date',
         'PY': 'pub year',
         'VL': 'volume',
         'IS': 'issue',
         'BP': 'beggining page',
         'EP': 'ending page',
         'DI': 'doi',
         'EC': 'scielo categories',
         'C2': 'scielo collection',
         'SC': 'research areas',
         'UT': 'accession number',
         'OA': 'open access indicator',
         'HC': 'highly cited',
         'HP': 'hot paper',
         'DA': 'report date'}
    df=df.rename(columns, axis=1)
    print(len(df))
    return df

def scielo_wos_info():

    info_dict = {}

    info_dict['Blah'] = \
           'https://images.webofknowledge.com/images/help/WOK/hs_selo_fieldtags.html\n'+\
           'SciELO Citation Index Field Tags\n' + \
           'These two-character field tags identify fields in records that you e-mail,'+\
           ' export, or save. They cover various publications.'

    info_dict['FN'] = 'File Name'
    info_dict['VR'] = 'Version Number'
    info_dict['PT'] = 'Publication Type'
    info_dict['AU'] = 'Authors'
    info_dict['BE'] = 'Editors'
    info_dict['TI'] = 'Title'

    '''
        S1
        Full Source Title (Korean or Other Languages)
        X1



        Spanish Document Title (A Spanish Document Title may have a field tag of T1, Y1, or Z1)
        Y1
        Portuguese Document Title (A Portuguese Document Title may have a field tag of T1, X1, or Z1)
        Z1
        Other Languages Document Title (A document title may have a field tag of T1, X1, or Y1)

        SO
        Source

        LA
        Language

        DT
        Document Type

        DE
        English Author Keywords

        X5
        Spanish Author Keywords

        Y5
        Portuguese Author Keywords

        Z5
        Author Keywords (Other Languages)

        AB
        English Abstract

        X4
        Spanish Abstract

        Y4
        Portuguese Abstract

        Z4
        Abstract (Other Languages)

        C1
        Addresses

        EM
        E-mail Address

        RI
        ResearcherID Number

        OI
        ORCID Identifier (Open Researcher and Contributor ID)

        CR
        Cited References

        NR
        Cited Reference Count

        TC
        SciELO Citation Index Times Cited Count

        Z9
        Total Times Cited Count (Web of Science Core Collection, BIOSIS Citation Index, Chinese Science Citation Database, Data Citation Index, Russian Science Citation Index, SciELO Citation Index)

        U1
        Usage Count (Last 180 Days)

        U2
        Usage Count (Since 2013)

        PU
        Publisher

        PI
        Publisher City

        PA
        Publisher Address

        SN
        International Standard Serial Number (ISSN)

        PD
        Publication Date

        PY
        Year Published

        VL
        Volume

        IS
        Issue

        BP
        Beginning Page

        EP
        Ending Page

        DI
        Digital Object Identifier (DOI)

        EC
        SciELO Categories

        C2
        SciELO Collection

        SC
        Research Areas

        UT
        Accession Number

        OA
        Open Access Indicator

        HP
        ESI Hot Paper. Note that this field is valued only for ESI subscribers

        HC
        ESI Highly Cited Paper. Note that this field is valued only for ESI subscribers

        DA
        Date this report was generated

        ER
        End of Record

        EF
        End of File

    '''
    return info_dict
