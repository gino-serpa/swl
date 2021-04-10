import pathlib
import pandas as pd
import chardet
import csv

countries ={'Algeria':      ['Algeria','Argelia'],
            'Albania':      ['Albania'],
            'Angola':       ['Angola'],
            'Argentina':    ['Argentina','República Argentina','Rep. Argentina'],
            'Australia':    ['Australia'],
            'Austria':      ['Austria'],
            'Azerbaijan':   ['Azerbaijan'],
            'Bangladesh':   ['Bangladesh'],
            'Barbados':     ['Barbados', 'BARBADOS'],
            'Belarus':      ['Belarus', 'BELARUS'],
            'Belgium':      ['Belgium','Bélgica'],
            'Benin':        ['Benin'],
            'Bhutan':       ['Bhutan'],
            'Bolivia':      ['Bolivia'],
            'Bosnia & Herceg':['Bosnia & Herceg'],
            'Botswana':     ['Botswana'],
            'Brazil':       ['Brazil','Brasil','BRAZIL', 'BR'],
            'Bulgaria':     ['Bulgaria'],
            'Burkina Faso':['Burkina Faso'],
            'Burundi':      ['Burundi'],
            'Canada':       ['Canada','CANADA','Canadá'],
            'Cabo Verde':   ['Cabo Verde'],
            'Cambodia':     ['Cambodia', 'CAMBODIA'],
            'Cameroon':     ['Cameroon'],
            'Czech Republic':['Czech Republic'],
            'China':        ['China','PEOPLES R CHINA','PEOPLES R CHINA',
                             "People's Republic of China",
                            'P. R. China',
                            'Republic of China'],
            'Colombia':     ['Colombia'],
            'Croatia':      ['Croatia'],
            'Cuba':         ['Cuba'],
            'Chile':        ['Chile'],
            'Colombia':     ['Colombia'],
            'Costa Rica':   ['Costa Rica'],
            'Cyprus':       ['Cyprus', 'CYPRUS'],
            'Denmark':      ['Denmark'],
            'Dominican Republic': ['Dominican Republic', 'República Dominicana',
                            'DOMINICAN REP'],
            'DR Congo':     ['DR Congo','Democratic Republic of the Congo',
                            'Republic of Congo'],
            'Ecuador':      ['Ecuador','República del Ecuador'],
            'Egypt':        ['Egypt'],
            'El Salvador':  ['El Salvador'],
            'Estonia':      ['Estonia'],
            'Ethiopia':     ['Ethiopia'],
            'Finland':      ['Finland'],
            'France':       ['France','Francia'],
            'French Guiana':['French Guiana'],
            'Gabon':        ['Gabon'],
            'Gambia':       ['Gambia'],
            'Germany':      ['Germany','Alemania','Deutschland', 'Alemanha'],
            'Ghana':        ['Ghana', 'GHANA'],
            'Greece':       ['Greece'],
            'Grenada':      ['Grenada'],
            'Guatemala':    ['Guatemala'],
            'Guinea':       ['Guinea'],
            'Guinea Bissau': ['Guinea Bissau'],
            'Guyana':       ['Guyana', 'GUYANA'],
            'Haiti':        ['Haiti', 'HAITI'],
            'Hong Kong':    ['Hong Kong'],
            'Honduras':     ['Honduras'],
            'Hungary':      ['Hungary', 'HUNGARY','Hungría'],
            'Iceland':      ['Iceland','ICELAND'],
            'Indonesia':    ['Indonesia'],
            'India':        ['India'],
            'Iran':         ['Iran'],
            'Iraq':         ['Iraq'],
            'Ireland':      ['Ireland', 'Irlanda'],
            'Israel':       ['Israel'],
            'Italy':        ['Italy','ITALY','Itália','Italia'],
            'Ivory Coast':  ['Ivory Coast',"Côte d'Ivoire"],
            'Jamaica':      ['Jamaica'],
            'Japan':        ['Japan', 'JAPAN', 'Japón', 'Japão'],
            'Jordan':       ['Jordan'],
            'Kazakhstan':   ['Kazakhstan'],
            'Kenya':        ['Kenya'],
            'Korea':        ['Korea','Coreia do Sul','SOUTH KOREA'],
            'Kosovo':       ['Kosovo'],
            'Laos':         ['Laos'],
            'Latvia':       ['Latvia'],
            'Liberia':      ['Liberia'],
            'Lebanon':      ['Lebanon'],
            'Lesotho':      ['Lesotho'],
            'Lithuania':    ['Lithuania'],
            'Luxembourg':   ['Luxembourg'],
            'Macedonia':    ['Macedonia'],
            'Madagascar':   ['Madagascar'],
            'Malaysia':     ['Malaysia'],
            'Malawi':       ['Malawi'],
            'Mali':         ['Mali'],
            'Malta':        ['Malta'],
            'Mexico':       ['Mexico', 'México'],
            'Moldova':      ['Moldova'],
            'Monaco':       ['Monaco'],
            'Montenegro':   ['Montenegro'],
            'Moroco':       ['Moroco', 'Morocco', 'Morrocco','Maroc'],
            'Mozambique':   ['Mozambique','Moçambique'],
            'Namibia':      ['Namibia'],
            'Nepal':        ['Nepal'],
            'Netherlands':  ['Netherlands', 'Holanda', 'The Netherlands',
                             'Países Bajos'],
            'New Zealand':  ['New Zealand', 'Nueva Zelanda'],
            'Nicaragua':    ['Nicaragua'],
            'Niger':        ['Niger'],
            'Nigeria':      ['Nigeria'],
            'North Ireland':['North Ireland'],
            'Norway':       ['Norway', 'Noruega'],
            'Oman':         ['Oman'],
            'Pakistan':     ['Pakistan'],
            'Palestine':    ['Palestine'],
            'Panama':       ['Panama','Panamá'],
            'Papua and Guinea':['Papua and Guinea','PAPUA N GUINEA'],
            'Paraguay':     ['Paraguay','Paraguai'],
            'Peru':         ['Peru', 'Perú'],
            'Philippines':  ['Philippines'],
            'Poland':       ['Poland','Polonia'],
            'Portugal':     ['Portugal'],
            'Puerto Rico':  ['Puerto Rico'],
            'Qatar':        ['Qatar','QATAR'],
            'Romania':      ['Romania'],
            'Russia':       ['Russia', 'Rusia', 'Russian Federation','Russiam'],
            'Rwanda':       ['Rwanda'],
            'Saint Kitts and Nevis': ['Saint Kitts and Nevis','St Kitts & Nevi'],
            'San Marino':   ['San Marino'],
            'Saudi Arabia': ['Saudi Arabia','Kingdom of Saudi Arabia',
                             'Arabia Saudita'],
            'Scotland':     ['Scotland'],
            'Senegal':      ['Senegal', 'Sénégal'],
            'Serbia':       ['Serbia'],
            'Singapore':    ['Singapore'],
            'Slovenia':     ['Slovenia'],
            'Slovakia':     ['Slovakia','SLOVAKIA'],
            'South Africa': ['South Africa'],
            'Sri Lanka':    ['Sri Lanka'],
            'Spain':        ['Spain','España','Espanha'],
            'Sudan':        ['Sudan'],
            'Sweden':       ['Sweden','Suécia'],
            'Switzerland':  ['Switzerland','Suíça'],
            'Syria':        ['Syria'],
            'Taiwan':       ['Taiwan'],
            'Tanzania':     ['Tanzania', 'United Republic of Tanzania'],
            'Thailand':     ['Thailand'],
            'Togo':         ['Togo'],
            'Trinidad and Tobago': ['TRINID TOBAGO','Trinidad and Tobago'],
            'Tunisia':      ['Tunisia'],
            'Turkey':       ['Turkey','Turquía'],
            'Uganda':       ['Uganda'],
            'Ukraine':      ['Ukraine'],
            'United Arab Emirates': ['United Arab Emirates','U Arab Emirates'],
            'United Kingdom': ['United Kingdom', 'UK', 'ENGLAND','Inglaterra',
                                'U.K','Reino Unido'],
            'Uruguay':      ['Uruguay','República Oriental del Uruguay'],
            'USA':          ['USA', 'Estados Unidos', 'United States','EE.UU',
                             'United States of América','EE. UU',
                             'United States of America',
                             'Estados Unidos de América',
                             'Estados Unidos da América','U.S.A','US',
                             'U. S. A'],
            'Venezuela':    ['Venezuela','República Bolivariana de Venezuela'],
            'Vietnam':      ['Vietnam', 'Viet Nam'],
            'Wales':        ['Wales'],
            'Zambia':       ['Zambia'] ,
            'Zimbabwe':     ['Zimbabwe']}

def ingest_folder(database, data_folder = pathlib.Path.cwd()/'data', encoding='unknown',  ):
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
        if database=='scielo':
            df_list.append(ingest_scielo_file(data_file, encoding))
        elif database == 'wos':
            df_list.append(ingest_wos_file(data_file, encoding))
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

def ingest_wos_file(file_name, encoding):
    '''
    Ingest an individual data file with data from wos
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
         'BA': 'book authors',
         'BE': 'editors',
         'GP': 'book group authors',
         'AF': 'author full name',
         'BF': 'book authors full name',
         'CA': 'group authors',
         'TI': 'title',
         'SO': 'source',
         'SE': 'book series title',
         'BS': 'book series subtitle',
         'LA': 'language',
         'DT': 'document type',
         'CT': 'conference title',
         'CY': 'conference date',
         'CL': 'conference location',
         'SP': 'conference sponsors',
         'HO': 'conference host',
         'DE': 'english author keywords',
         'ID': 'keywords plus',
         'AB': 'abstract',
         'C1': 'addresses',
         'RP': 'reprint address',
         'EM': 'emails ',
         'RI': 'research id number',
         'OI': 'orchid id',
         'FU': 'funding agency and grant number',
         'FX': 'funding text',
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
         'EI': 'eissn',
         'BN': 'isbn',
         'J9': '29-character source abbreviation',
         'JI': 'iso source abbreviation',
         'PD': 'pub date',
         'PY': 'pub year',
         'VL': 'volume',
         'IS': 'issue',
         'PN': 'part number',
         'SU': 'supplement',
         'SI': 'special issue',
         'MA': 'meeting abstract',
         'BP': 'beggining page',
         'EP': 'ending page',
         'AR': 'article number',
         'DI': 'doi',
         'D2': 'book doi',
         'EA': 'early access date',
         'PG': 'page count',
         'WC': 'wos categories',
         'SC': 'research areas',
         'GA': 'document delivery number',
         'UT': 'accession number',
         'PM': 'pubmed id',
         'OA': 'open access indicator',
         'HC': 'highly cited',
         'HP': 'hot paper',
         'DA': 'report date'}
    df=df.rename(columns, axis=1)
    print(len(df))
    return df

def get_scielo_dicts(df):
    authors = {}
    papers  = {}
    institutions = {}

    for idx,row in df.iterrows():
        # Extract fields
        id            = row['accession number']
        title         = row['title']
        spanish_title = row['spanish title']
        portuguese_title = row['portuguese title']
        other_language_title = row['other language title']
        source = row['source']
        language = row['language']
        english_author_keywords = \
                get_english_author_keywords(row['english author keywords'])
        authors_list = get_author_list(row['authors'])
        try:
            year = int(row['pub year'])
        except:
            continue
        addresses = get_addresses(row['addresses'])
        institution_list = list(set(list(addresses.values())))

        # Take care of papers dict
        papers[id] = {
               'title':title,
               'authors': authors_list,
               'year': year,
               'spanish title': spanish_title,
               'portuguese title': portuguese_title,
               'other language title': other_language_title,
               'source': source,
               'language': language,
               'english author keywords':english_author_keywords
                    }

        # Take care of the authors dict
        #print('authors_list: ', authors_list)
        for author in authors_list:
            #print('author:', author)
            if author not in authors:
                authors[author] = {'papers_list':[id]}
                authors[author]['institutions']  = []
            else:
                authors[author]['papers_list'].append(id)

#        for item in list(authors.keys()):
#            if 'Plase' in item:
#                print (item)

        #print('addresses: ', addresses)
        for author in addresses:
            institution = addresses[author]
            if institution not in authors[author]['institutions']:
                authors[author]['institutions'].append(institution)

        # Take care of institutions
        institution_names_list=[]
        for institution in institution_list:
            institution_name = institution.split(',')[0].strip(' ')
            institution_names_list.append(institution_name)
            if institution_name not in institutions:
                country = institution.split(',')[-1].strip(' ')
                country = get_valid_country(country)
                institutions[institution_name]=\
                    {'papers':[id],
                    'country':country}
            else:
                institutions[institution_name]['papers'].append(id)
        papers[id]['institutions']=institution_names_list

    return authors, papers, institutions

def get_wos_dicts(df):
    authors = {}
    papers  = {}
    institutions = {}

    for idx,row in df.iterrows():
        # Extract fields
        id     = row['accession number']
        title  = row['title']
        source = row['source']
        language = row['language']
        english_author_keywords = \
                get_english_author_keywords(row['english author keywords'])
        authors_list = get_author_list(row['author full name'])
        try:
            year = int(row['pub year'])
        except:
            continue
        addresses = get_addresses(row['addresses'])
        institution_list = list(set(list(addresses.values())))

        # Take care of papers dict
        papers[id] = {
               'title':title,
               'authors': authors_list,
               'year': year,
               'source': source,
               'language': language,
               'english author keywords':english_author_keywords
                    }

        # Fill the authors dict with the authors as keys
        # and assign the paper to the author
        for author in authors_list:
            if author not in authors:
                authors[author] = {'papers_list':[id]}
                authors[author]['institutions']  = []
            else:
                authors[author]['papers_list'].append(id)

        # Add institutions to author (unless they are already there)
        for author in addresses:
            institution = addresses[author]
            if author not in authors:
                print('Possible bad input data: ', author)
            else:
                if institution not in authors[author]['institutions']:
                    authors[author]['institutions'].append(institution)

        # Take care of institutions
        institution_names_list=[]
        for institution in institution_list:
            institution_name = institution.split(',')[0].strip(' ')
            institution_names_list.append(institution_name)
            if institution_name not in institutions:
                country = institution.split(',')[-1].strip(' ')
                country = get_valid_country(country)
                institutions[institution_name]=\
                    {'papers':[id],
                    'country':country}
            else:
                institutions[institution_name]['papers'].append(id)
        papers[id]['institutions']=institution_names_list

    return authors, papers, institutions

def get_english_author_keywords(keyword_string):
    '''
    Returns a list of english author keywords
        Input:
            keyword_string: string with keyword information
        Returns:
            list of keywords
    '''
    if keyword_string!=keyword_string:
        return []
    english_author_keywords = keyword_string.split('; ')
    return english_author_keywords

def get_author_list(author_str):
    if author_str!=author_str:
        return []
    author_list = author_str.split('; ')
    author_list = [item.replace('.',' ').strip(' ').replace('  ',' ') \
                    for item in author_list]

    author_list = [item.strip("' ").replace('  ',' ') \
                    for item in author_list]
    return author_list

def get_addresses(alpha):
    if alpha!=alpha:
        return {}
    # Define an empty dict that will have the info we need
    addresses = {}

    # Break by the leading '[' of each author group
    alpha = alpha.split('[')[1:]

    # Each group now is divided in authors and an institution
    groups = [ item.split(']') for item in alpha]

    # Clean up each group and assign info to dict
    for pair in groups:
        if len(pair)!=2:
            print('Badly written pair: ', pair, ' Should be exactly 2 elements')
            return addresses
        (people, place) = pair
        place = place.strip('; ')
        people = people.split('; ')
        people = [item.replace('.', ' ').strip(' ').replace('  ',' ') \
                         for item in people]
        # Too many spaces, perhaps use ' '.join(mystring.split())
        people = [item.replace('.', ' ').strip(' ').replace('  ',' ') \
                                 for item in people]
        for author in people:
            addresses[author]=place
    return addresses

def get_valid_country(country):
    '''
    Returns a valid country alias

    Input:
        country: string with the country as mentioned in the institution string
    Returns:
        canonical_name: a valid country canonical name or 'not in database'
                        if country could not be matched against the countries
                        dict
    '''
    country=country.strip('.')
    if country.endswith(' USA'):
        country = 'USA'
    for canonical_name in countries:
        for alias in countries[canonical_name]:
            if alias.lower()==country.lower():
                return canonical_name
    print('Country: '+ country +' not in database' )
    return 'No country available'

def scielo_info():

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
    info_dict['S1'] = 'Full Source Title (Korean or Other Languages)'
    info_dict['X1'] = 'Spanish Document Title'
    info_dict['Y1'] = 'Portuguese Document Title'
    info_dict['Z1'] = 'Other Languages Document Title'
    info_dict['SO'] = 'Source'
    info_dict['LA'] = 'Language'
    info_dict['DT'] = 'Document Type'
    info_dict['DE'] = 'English Author Keywords'
    info_dict['X5'] = 'Spanish Author Keywords'
    info_dict['Y5'] = 'Portuguese Author Keywords'
    info_dict['Z5'] = 'Author Keywords (Other Languages)'

    '''
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

'''
WOS field tags from
https://images.webofknowledge.com/images/help/WOS/hs_wos_fieldtags.html

FN: 	File Name
VR:     Version Number
PT: 	Publication Type (J=Journal; B=Book; S=Series; P=Patent)
AU: 	Authors
AF:     Author Full Name
BA:     Book Authors
BF:     Book Authors Full Name
CA:     Group Authors
GP:     Book Group Authors
BE:     Editors
TI:     Document Title
SO:     Publication Name
SE:     Book Series Title
BS:     Book Series Subtitle
LA:     Language
DT: 	Document Type
CT: 	Conference Title
CY:     Conference Date
CL: 	Conference Location
SP: 	Conference Sponsors
HO: 	Conference Host
DE: 	Author Keywords
ID: 	Keywords Plus®
AB:     Abstract
C1: 	Author Address
RP: 	Reprint Address
EM: 	E-mail Address
RI: 	ResearcherID Number
OI: 	ORCID Identifier (Open Researcher and Contributor ID)
FU: 	Funding Agency and Grant Number
FX: 	Funding Text
CR:     Cited References
NR:     Cited Reference Count
TC:     Web of Science Core Collection Times Cited Count
Z9:     Total Times Cited Count (Web of Science Core Collection, Arabic Citation Index, BIOSIS Citation Index, Chinese Science Citation Database, Data Citation Index, Russian Science Citation Index, SciELO Citation Index)
U1:     Usage Count (Last 180 Days)
U2:     Usage Count (Since 2013)
PU:     Publisher
PI:     Publisher City
PA:     Publisher Address
SN:     International Standard Serial Number (ISSN)
EI:     Electronic International Standard Serial Number (eISSN)
BN:     International Standard Book Number (ISBN)
J9:     29-Character Source Abbreviation
JI:     ISO Source Abbreviation
PD:     Publication Date
PY: 	Year Published
VL: 	Volume
IS: 	Issue
SI: 	Special Issue
PN: 	Part Number
SU: 	Supplement
MA: 	Meeting Abstract
BP: 	Beginning Page
EP: 	Ending Page
AR:     Article Number
DI: 	Digital Object Identifier (DOI)
D2: 	Book Digital Object Identifier (DOI)
EA: 	Early access date
EY: 	Early access year
PG:     Page Count
P2: 	Chapter Count (Book Citation Index)
WC: 	Web of Science Categories
SC: 	Research Areas
GA: 	Document Delivery Number
PM: 	PubMed ID
UT: 	Accession Number
OA:     Open Access Indicator
HP:     ESI Hot Paper. Note that this field is valued only for ESI subscribers.
HC:     ESI Highly Cited Paper. Note that this field is valued only for ESI subscribers.
DA:     Date this report was generated.
ER:     End of Record
EF:     End of File
'''
