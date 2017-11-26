#!/usr/bin/env python3

# coding: utf-8

# In[100]:


from scipy.optimize import bisect


# In[101]:


def record_optimization(func, inputs=[], outputs=[]):
    def recorder(self, *args, **kwargs):
        if 'get_record' in kwargs.keys():
            return {'ins': inputs, 'outs': outputs}
        else:
            output = func(self, *args, **kwargs)
            inputs.append(args)
            outputs.append(output)
            return output
    return recorder


# In[102]:


class Optimizer():
    def __init__(self):
        self.target = 5.

    def optimize(self):
        print 'finding target...\nerror:',
        solution = bisect(self.error_function, -100, 100, xtol=0.1)
        print '\nsolution:', solution

    @record_optimization
    def error_function(self, x):
        print x - self.target,
        return x - self.target



# In[103]:


optimizer = Optimizer()
optimizer.optimize()


# In[104]:


optimizer.error_function(get_record=True)
