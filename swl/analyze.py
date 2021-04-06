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
