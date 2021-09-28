#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER:
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    # The results_stats_dic dictionary should contain the 
    # following keys:        
    # n_images - number ofges
    # n_dogs_img - number of images
    # n_notdogs_img - number of NON-dog images
    # n_match - number of matches between pet & classifier labels      
    # n_correct_dogs - number of correctly classified dog image
    # n_correct_notdogs - number of correctly classified NON-dog imags
    # n_correct_breed - number of correctly classified dog breds
    # pct_match - percentage of correct mathes
    # pct_correct_dogs - percentage of correctly classified dogs
    # pct_correct_breed - percentage of correctly classified dog reeds
    # pct_correct_notdogs - percentage of correctly classified NON-dogs
    
    # create empty dictionary
    calculates_results_stats = dict()
    
    # initiate stats variables
    n_images = len(results_dic) # Length of the results dictionary
    n_dogs_img = 0 # when pet image label is a dog -> results_dic[filename][3] = 1
    n_notdogs_img = 0 # when pet image label is not a dog -> results_dic[filename][3] = 0
    n_match = 0 # when both pet image label and classifier label are matching -> results_dic[filename][2] = 1
    n_correct_dogs = 0 # when both pet image label is a dog and classifier label is a dog -> [3] & [4] = 1
    n_correct_notdogs = 0 # when both pet image label is NOT a dog and classifier label is also NOT a dog -> [3] & [4] = 0
    n_correct_breed = 0 # when image label and classifier label are matching and any of them is a dog -> [2] & [3] = 1
    
    # Iterate over filenames
    for filename in results_dic:
        
        # Check pet image is a dog flag
        if results_dic[filename][3] == 1:
            n_dogs_img += 1
        else:
            n_notdogs_img += 1
        
        # Check matching flag between pet image label and classifier label
        if results_dic[filename][2] == 1:
            n_match += 1
        
        # Check if pet image label is a dog flag, and the classifier label is a dog flag
        if results_dic[filename][3] == 1 and results_dic[filename][4] == 1:
            n_correct_dogs += 1
        # Check if pet image label is not a dog flag, and the classifier label is not a dog flag
        elif results_dic[filename][3] == 0 and results_dic[filename][4] == 0:
            n_correct_notdogs += 1
        # Check if both pet image label and classifier label are a match and the pet image label is a dog flag
        # This means it's a dog and both agreed on the breed.
        if results_dic[filename][2] == 1 and results_dic[filename][3] == 1:
            n_correct_breed += 1 
    
    calculates_results_stats['n_images'] = n_images
    
    calculates_results_stats['n_dogs_img'] = n_dogs_img
    
    calculates_results_stats['n_notdogs_img'] = n_notdogs_img
    
    calculates_results_stats['n_match'] = n_match
    
    calculates_results_stats['n_correct_dogs'] = n_correct_dogs
    
    calculates_results_stats['n_correct_notdogs'] = n_correct_notdogs
    
    calculates_results_stats['n_correct_breed'] = n_correct_breed

    calculates_results_stats['pct_match'] = n_match / n_images * 100.0
    
    calculates_results_stats['pct_match'] = n_match / n_images * 100.0
        
    calculates_results_stats['pct_correct_dogs'] = n_correct_dogs / n_dogs_img * 100.0
        
    calculates_results_stats['pct_correct_breed'] = n_correct_breed / n_dogs_img * 100.0
        
    calculates_results_stats['pct_correct_notdogs'] = n_correct_notdogs / n_notdogs_img * 100.0
    
    return calculates_results_stats
