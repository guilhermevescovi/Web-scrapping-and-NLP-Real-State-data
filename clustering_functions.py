from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# we define a function that gives the Squared Sum distance for a matrix in a range K
def elbow_values(K,matrix,ret = False):

    mms = StandardScaler()
    mms.fit(matrix)
    data_transformed = mms.transform(matrix)
    
    SSD = []

    # for each cluster we compute his SSD
    for k in K:
        km = KMeans(n_clusters=k)
        km = km.fit(data_transformed)
        km = km.inertia_
        # we print it
        print('N_Cluster='+str(k),'SSD='+str(km))
        # and save it
        SSD.append(km)
    
    if ret:
        return(SSD)
        
# we write now a function that given our two matrix and how many cluster we need per matrix it return the list of clusters
def find_clusters(features_N_clusters, features_matrix, descriptions_N_clusters, description_matrix):
    
    clustered_features = KMeans(n_clusters=features_N_clusters).fit(features_matrix)
    clustered_descriptions = KMeans(n_clusters=descriptions_N_clusters).fit(description_matrix)
        
    features_cluster_list = []
    for i in range(features_N_clusters):
        features_cluster_list.append(all_indices(i,list(clustered_features.labels_)))
            
    descriptions_cluster_list = []
    for i in range(descriptions_N_clusters):
        descriptions_cluster_list.append(all_indices(i,list(clustered_descriptions.labels_)))
    
    return (features_cluster_list, descriptions_cluster_list)

# we define a function that five a value and a list give as output the set of indices of the list contaning the value
def all_indices(value, qlist):
    indices = []
    idx = -1
    while True:
        try:
            idx = qlist.index(value, idx+1)
            indices.append(idx)
        except ValueError:
            break
    return set(indices)

# we write a function that give the jaccard similarity for two sets
def jaccard_sim(S1,S2):
    intl = len(S1.intersection(S2))
    unil = len(S1.union(S2))
    return intl/unil

# we iter all the cluster getting the jaccard similarity
def jaccard_sim_matrix(setlist1, setlist2):
    results_list = []
    for S1 in setlist1:
        l = []
        for S2 in setlist2:
            l.append(jaccard_sim(S1,S2))
        results_list.append(l)
    return results_list