def normalize_features(filters_scores_dict):
  # Normalize: upper limit for tweeting is one tweet per minute; divide the returned average per day by max tweets per day
  filters_scores_dict['tweets_per_day_ratio'] /= 60 * 24;   
  # Normalize: turn eny boolean res into an integer value
  for filter_name, res in filters_score_dict:
    if type(res) == bool:
      filters_scores_dict[filter_name] = int(res)
  # Normalize: divide active hour by total hours in a day
  filters_scores_dict['hours_per_day'] /= 24

def knn_classifier(user):
  pass
