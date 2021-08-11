#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#DESCRIPTIVE STATISTICS [NUMERICAL PART]


# In[ ]:


#Topic is "MEAN"


# In[2]:


#"PYTHON"
import numpy
values = [4,11,7,14]
x = numpy.mean(values)
print(x)


# In[ ]:


'''
"R"
values <- c(4,7,11,14)
mean(values)
O/P:9
'''


# In[ ]:


#Topic is "MEDIAN"


# In[5]:


#"PYTHON"
import numpy
values = [13,21,21,40,42,48,55,72]
x = numpy.median(values)
print(x)


# In[ ]:


'''
"R"
values <- c(13,21,21,40,42,48,55,72)
median(values)
O/P:41
'''


# In[ ]:


#Topic is "MODE"


# In[6]:


#"PYTHON"
from statistics import multimode
values = [4,7,3,8,11,7,10,19,6,9,12,12]
x = multimode(values)
print(x)


# In[ ]:


'''
"R"
mode<- finction(x)
{
unique_values <- unique(x)
table <- tabulate(match(x,unique_values))
unique_values[table==max(table)]
}
values <- c[4,7,3,8,11,7,10,19,6,9,12,12]
mode(values)
O/P:7 12 
'''


# In[ ]:


#Topic is "STANDARD DEVIATION"


# In[8]:


#"PYTHON"
#"POPULATION"
import numpy
values = [4,11,7,14]
x = numpy.std(values)
print(x)


# In[ ]:


'''
"R"
"POPULATION"
values <- c(4,7,11,14)
sqrt(mean(values-mean(values))^2))
O/P:3.8078655
'''


# In[9]:


#"PYTHON"
#"SAMPLE"
import numpy
values = [4,11,7,14]
x = numpy.std(values,ddof=1)
print(x)


# In[ ]:


'''
"R"
"SAMPLE"
values <- c(4,7,11,14)
sd(values)
O/P:3.81
'''


# In[ ]:


#Topic is "RANGE"


# In[16]:


#"PYTHON"
import numpy
values = [13,21,21,40,42,48,55,72]
x = numpy.ptp(values)
print(x)


# In[ ]:


'''
"R"
values <- c(13,21,21,40,42,48,55,72)
max(values)-min(values)
O/P:59  
'''


# In[ ]:


#Topic is "QUARTILES"


# In[11]:


#"PYTHON"
import numpy
values = [13,21,21,40,42,48,55,72]
x = numpy.quantile(values,[0,0.25,0.5,0.75,1])
print(x)


# In[ ]:


'''
"R"
values <- c(13,21,21,40,42,48,55,72)
quantile(values)
O/P:13.   21.   41.   49.75 72.  
'''


# In[ ]:


#Topic is "PERCENTILES"


# In[12]:


#"PYTHON"
import numpy
values = [13,21,21,40,42,48,55,72]
x = numpy.percentile(values,65)
print(x)


# In[ ]:


'''
"R"
values <- c(13,21,21,40,42,48,55,72)
quantile(values,0.65)
O/P:45.3 (#that is 65%)
'''


# In[ ]:


#Topic is "INTERQARTILE RANGE"


# In[14]:


#"PYTHON"
from scipy import stats
values = [13,21,21,40,42,48,55,72]
x = stats.iqr(values)
print(x)


# In[ ]:


'''
"R"
values <- c(13,21,21,40,42,48,55,72)
IQR(values)
O/P:28.75
'''


# In[ ]:


#DESCRIPTIVE STATISTICS [VISUALIZATION TECHNIQUE]


# In[ ]:


#Topic is Bar Graph
#Topic is Box Plot
#Topic is Histograms
#Topic is Skewness and Kurtosis


# In[ ]:




