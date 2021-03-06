from collections import Counter
import matplotlib.pyplot as plt

def get_country_papers_count(papers, institutions):
    country_papers_count = {}
    for paper in papers:
        countries_in_paper=[]
        for institution in papers[paper]['institutions']:
            country =institutions[institution]['country']
            if country not in countries_in_paper:
                countries_in_paper.append(country)
        for country in countries_in_paper:
            if country not in country_papers_count:
                country_papers_count[country]=1
            else:
                country_papers_count[country]+=1
    return country_papers_count

def country_papers_hist(country_papers_count):

    from operator import itemgetter, attrgetter

    plt.style.use('ggplot')

    country_papers_list = list(country_papers_count.items())
    countries_papers_list = sorted(country_papers_list, key=itemgetter(1), reverse=True)
    n_countries = 28
    countries = [country for (country,papers) in countries_papers_list] [0:n_countries][::-1]
    papers_numbers = [papers for (country,papers) in countries_papers_list][0:n_countries][::-1]

    y_pos = [i for i, _ in enumerate(countries)]
    plt.figure(figsize=(14,8))
    plt.barh(y_pos, papers_numbers, color='green')
    plt.ylabel('Country')
    plt.xlabel('Number of papers')
    plt.title('Number of papers in gender studies per country (Scielo)')

    plt.yticks(y_pos, countries)

    plt.show()
    return

def plot_country_papers_time(country, papers, institutions):
    years=[]
    for paper in papers:
        year = papers[paper]['year']
        for institution in papers[paper]['institutions']:
            if institutions[institution]['country']==country:
                years.append(year)
                break
    years_papers_dict = Counter(years)
    years =  sorted(list(years_papers_dict.keys()))
    papers_per_year = [years_papers_dict[year] for year in years]
    plt.plot(years,papers_per_year)
    plt.title(country)
    plt.xlabel('years')
    plt.ylabel('papers')
    plt.show()

    return

def view_inst_papers_hist(institutions, n=30):
    inst_papers_list = [(inst+', '+institutions[inst]['country'], len(institutions[inst]['papers'])) \
                         for inst in institutions]
    inst_papers_list=sorted(inst_papers_list,key=lambda x:x[1], reverse=True)[0:n]

    insts = [inst for (inst, papers) in inst_papers_list][::-1]
    papers_numbers = [papers for (inst,papers) in inst_papers_list][::-1]

    y_pos = [i for i, _ in enumerate(insts)]
    plt.figure(figsize=(14,8))
    plt.barh(y_pos, papers_numbers, color='green')
    plt.ylabel('Institution')
    plt.xlabel('Number of papers')
    plt.title('Top publishing institutions')

    plt.yticks(y_pos, insts)

    plt.show()

    return

def plot_country_institutions(country, institutions):
    country_inst_papers = [ (inst, len(institutions[inst]['papers'])) \
                            for inst in institutions \
                            if institutions[inst]['country']==country ]
    country_inst_papers = sorted(country_inst_papers,
                                 key=lambda x:x[1],
                                 reverse=True)
    n_inst = min([len(country_inst_papers),10])

    country_institutions = [ item[0] for item in country_inst_papers][0:n_inst][::-1]
    institution_papers = [ item[1] for item in country_inst_papers][0:n_inst][::-1]

    y_pos = [i for i, _ in enumerate(country_institutions)]
    plt.figure(figsize=(14,8))
    plt.barh(y_pos, institution_papers, color='green')
    plt.ylabel('Institution')
    plt.xlabel('Number of papers')
    plt.title('Top publishing institutions in: '+ country)

    plt.yticks(y_pos, country_institutions)

    plt.show()

    return


def plot_output_time(papers):
    years=[]
    for paper in papers:
        year = papers[paper]['year']
        years.append(year)
    years_papers_dict = Counter(years)

    years =  sorted(list(years_papers_dict.keys()))
    papers_per_year = [years_papers_dict[year] for year in years]
    plt.plot(years,papers_per_year)
    plt.show()

    return

def plot_region_papers_time(region, papers, institutions):
    years=[]
    for paper in papers:
        year = papers[paper]['year']
        for institution in papers[paper]['institutions']:
            if institutions[institution]['country'] in region:
                years.append(year)
                break
    years_papers_dict = Counter(years)
    years =  sorted(list(years_papers_dict.keys()))
    papers_per_year = [years_papers_dict[year] for year in years]

    plt.plot(years,papers_per_year)
    plt.title(str(region))
    plt.xlabel('years')
    plt.ylabel('papers')
    plt.show()

    return


def compare_growth_rates(papers1, papers2):

    years=[]
    for paper in papers1:
        year = papers1[paper]['year']
        years.append(year)
    years1_papers_dict = Counter(years)

    years=[]
    for paper in papers2:
        year = papers2[paper]['year']
        years.append(year)
    years2_papers_dict = Counter(years)

    years =  sorted(list(years1_papers_dict.keys()))
    years=years[0:-1]
    papers_py1 = [years1_papers_dict[year] for year in years]
    papers_py2 = [years2_papers_dict[year] for year in years]
    ratio   = [np1/np2 for (np1,np2) in zip(papers_py1,papers_py2)]
    #papers_per_year = [years_papers_dict[year] for year in years]
    #plt.plot(years,papers_per_year)
    plt.plot(years, ratio)

    plt.show()

    return


def get_authors_history(author_int_list,
                        authors_wos, papers_wos,
                        authors_scielo, papers_scielo):

    authors_history = {}
    for author in author_int_list:
        authors_history[author] =  get_author_individual_history(author,
                                                                 authors_wos,
                                                                 papers_wos,
                                                                 authors_scielo,
                                                                 papers_scielo)

    return authors_history

def get_author_individual_history(author,
                                  authors_wos, papers_wos,
                                  authors_scielo, papers_scielo):
    history  = {'wos':{},'scielo':{},'overlap':{},
                'wos_doi':[], 'scielo_doi':[]}

    # First the wos DOI's
    for paper in authors_wos[author]['papers_list']:
        doi = papers_wos[paper]['doi']
        history['wos_doi'].append(doi)

    # Now the scielo DOI's
    for paper in authors_scielo[author]['papers_list']:
        doi = papers_scielo[paper]['doi']
        history['scielo_doi'].append(doi)

    # Now for the keys [wos, scielo, overlap]

    # Check the scielo papers
    for paper in authors_scielo[author]['papers_list']:
        doi = papers_scielo[paper]['doi']
        year= papers_scielo[paper]['year']

        # Check for overlap
        if doi in history['wos_doi']:
            if year in history['overlap']:
                history['overlap'][year]+=1
            else:
                history['overlap'][year]=1
        else:
            if year in history['scielo']:
                history['scielo'][year]+=1
            else:
                history['scielo'][year]=1

    # Check the WOS papers
    for paper in authors_wos[author]['papers_list']:
        doi = papers_wos[paper]['doi']
        year = papers_wos[paper]['year']

        # Check for overlap
        if doi not in history['scielo_doi']:
            if year in history['wos']:
                history['wos'][year] += 1
            else:
                history['wos'][year] =1

    return history

def get_global_history(history):

    global_history ={'scielo': {}, 'wos':{}, 'overlap':{}}

    for author in history:
            # get time0:
            years = list(history[author]['scielo'].keys())+\
                    list(history[author]['overlap'].keys())+\
                    list(history[author]['wos'].keys())
            time0 = min(years)
            #print(author)
            #print(history[author])
            #print(time0)

            # Construct shifted paper count dicts
            scielo_shifted_h = {key-time0:value for key,value in history[author]['scielo'].items()}
            overlap_shifted_h = {key-time0:value for key,value in history[author]['overlap'].items()}
            wos_shifted_h = {key-time0:value for key,value in history[author]['wos'].items()}

            # Accumulate the shifted dictionaries in the glabal history
            # scielo
            for key, value in scielo_shifted_h.items():
                if key in global_history['scielo']:
                    global_history['scielo'][key]+=value
                else:
                    global_history['scielo'][key]=value
            # overlap
            for key, value in overlap_shifted_h.items():
                if key in global_history['overlap']:
                    global_history['overlap'][key]+=value
                else:
                    global_history['overlap'][key]=value
            # wos
            for key, value in wos_shifted_h.items():
                if key in global_history['wos']:
                    global_history['wos'][key]+=value
                else:
                    global_history['wos'][key]=value

    return global_history
