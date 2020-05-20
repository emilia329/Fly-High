def Airlines(df):
    plt.xlabel("AIRLINES")
    plt.ylabel("FREQU")
    df.value_counts().plot(kind='bar',title='AIRLINES', color ='cornflowerblue').get_figure().savefig('airport_airlines.png',dpi=None,bbox_inches = 'tight')
    fig= plt.figure(figsize=(18,5))
    
    
def airline(df):   
    f, ax = plt.subplots(figsize=(18,5)) 

    ### Setting the labels of the X axis
    labels = ['JAN','FEB','MARCH','APRIL','MAY','JUNE','JULY','AUG','SEPT','OCT','NOV','DEC']

    ontime = df[df['class'] ==3].groupby(['MONTH']).size()
    delay = df[df['class'] ==2].groupby(['MONTH']).size()
    ### X- Label locations 
    x = np.arange(len(labels))  
    ### Width of the bars
    width = 0.30  
    ### Code to plot the bars 
    rect1= ax.bar(x - width/2, ontime, width, label = 'On Time',color = 'coral')
    rect2= ax.bar(x + width/2, delay, width, label = 'Delay',color = 'cornflowerblue')

    ### Set the x-ticks
    ax.set_xticks(x)
    ### Setting labels 
    ax.set_xticklabels(labels)
    ### Labeling the X axis
    ax.set_xlabel(" Months")
    ### Y axis Label
    ax.set_ylabel("# of Flights ")
    ### Title of Graoh
    ax.set_title(" Airline")
    ### Showing the legend 
    ax.legend(ncol=1)
    ### Show graph
    plt.savefig('airlines.png',dpi=None,bbox_inches = 'tight')
    plt.show()

def cancellation(df):    
    sns.set_style('white')
    fig = plt.figure(figsize = (21,15))
    fig.subplots_adjust(hspace = .30)
    #labels = ['JAN','FEB','MARCH','APRIL','MAY','JUNE','JULY','AUG','SEPT','OCT','NOV','DEC']
    width = 0.30
    ax1 = fig.add_subplot(221)
    ax1.hist(df[df['class']==1].MONTH,  bins = 12, label = 'Cancelled ', alpha = .90, edgecolor = 'black',color = 'lightsalmon')
    
    ax1.set_title('Cancelled Flights',fontsize=18)
    ax1.set_xticks(range(1,13))
    ax1.set_xlabel('Months of the year')
    ax1.set_ylabel('# of Flights')
    ax1.legend(loc = 'upper right')
    plt.show()
    
    
def delays(df):   
    sns.set_style('white')
    fig = plt.figure(figsize = (21,15))
    #fig.subplots_adjust(hspace = .30)

    ax1 = fig.add_subplot(222)
    ax1.hist(df[df['delay_nas']==True].MONTH,  bins = 12, label = 'NAS', alpha = .90, edgecolor = 'black',color = 'lightgreen')
    ax1.hist(df[df['delay_carrier']==True].MONTH,  bins = 12, label = 'Carrier', alpha = .90, edgecolor = 'black',color = 'pink')
    ax1.hist(df[df['delay_late_aircraft']==True].MONTH,  bins = 12, label = 'Late Aircraft', alpha = .90, edgecolor = 'black',color = 'coral')
    ax1.hist(df[df['delay_weather']==True].MONTH,  bins = 12, label = 'Weather', alpha = .90, edgecolor = 'black',color = 'lightblue')
    ax1.hist(df[df['delay_security']==True].MONTH,  bins = 1, label = 'Security', alpha = .90, edgecolor = 'black',color = 'black')

    ax1.set_title('Airline Reason for Delay',fontsize=18)
    ax1.set_xticks(range(1,13))

    ax1.set_xlabel('Months of the year')
    ax1.set_ylabel('# of Flights')
    ax1.legend(loc = 'upper right')
    plt.show()    
    
    
#Model


def airportgraph(df):

    print(df['class'].value_counts())

    sns.set_style('darkgrid')
    plt.figure(figsize = (10,5))
    sns.countplot(df['class'], alpha =.80, palette= ['grey','coral','cornflowerblue'])
    plt.title('Cancelled, Delay, On Time Flights')
    plt.ylabel('# Passengers')
    plt.show()
    #plt.savefig('graph2.png',dpi=None,bbox_inches = 'tight')

def featureimport(X,y):    
    model = ExtraTreesClassifier()
    model.fit(X,y)
    print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
    #plot graph of feature importances for better visualization
    feat_importances = pd.Series(model.feature_importances_, index=X.columns)
    feat_importances.nlargest(10).plot(kind='barh', color='cornflowerblue')
    plt.title('Feature Importance')
    #plt.savefig('graph9.png',dpi=None,bbox_inches = 'tight')
    plt.show()
    
    
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Greens):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=2)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion Matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.3f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
    
def datatable(y_test,pred):
    data = { 
        'Micro': [ 
    precision_score(y_test,pred, 
                                               pos_label='positive',
                                               average='micro'),
    recall_score(y_test,pred, 
                                               pos_label='positive',
                                               average='micro'),
    f1_score(y_test,pred, 
                                               pos_label='positive',
                                               average='micro')],

        'Macro': [
            precision_score(y_test,pred, 
                                               pos_label='positive',
                                               average='macro'),
    recall_score(y_test, pred, 
                                               pos_label='positive',
                                               average='macro'),
    f1_score(y_test, pred, 
                                               pos_label='positive',
                                               average='macro')],
        'Weighted':[
       precision_score(y_test,pred, 
                                               pos_label='positive',
                                               average='weighted'),
    recall_score(y_test, pred, 
                                               pos_label='positive',
                                               average='weighted'),
    f1_score(y_test,pred, 
                                               pos_label='positive',
                                               average='weighted')]}

    return pd.DataFrame(data,
                      index=pd.Index(['Precison', 'Recall', 'F1 Score', ], ),
                      columns=pd.Index(['Micro', 'Macro', 'Weighted'],))    

def percentage(df):

    ontime = len(df[df['class']==3])
    delay = len(df[df['class']==2])
    cancelled = len(df[df['class']==1])
    pct_ontime = ontime/(ontime+delay+cancelled)
    pct_delay = delay/(ontime+delay+cancelled)
    pct_cancelled = cancelled/(ontime+delay+cancelled)
    print("percentage of ontime flights is", pct_ontime*100)
    print("percentage of delay flights is", pct_delay*100)
    print("percentage of cancelled flights", pct_cancelled*100)