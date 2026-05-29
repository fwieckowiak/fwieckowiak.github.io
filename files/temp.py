#%% open C:\Users\fwieckowiak\OneDrive - Luminess\Documents\mygithubpage\fwieckowiak.github.io\files\patent_numbers_query.txt
#and count the number of "or" in the file
with open(r"C:\Users\fwieckowiak\OneDrive - Luminess\Documents\mygithubpage\fwieckowiak.github.io\files\patent_numbers_query.txt", "r") as f:
    data = f.read()
    count_or = data.count("or")
    print(count_or) 
# %%
