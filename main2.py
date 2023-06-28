levels = {
            1: {     
                'weapons': ['sword'],    
                'time': 120,    
                'enemies': [
                    {
                        'type': 'earth',
                        'subtype': {
                            1: {
                                'total': 100,
                                'interval_time': 3
                            },                            
                        },
                        
                    },
                    {
                        'type': 'fly',
                        'subtype': {
                            1: {
                                'total': 100,
                                'interval_time': 3
                            },
                            2: {
                                'total': 40,
                                'interval_time': 5
                            }
                        },
                        
                    },
                    
                ]
            },
            2: {     
                'weapons': ['sword', 'gun'],    
                'time': 120,     
                'enemies': [
                    {
                        'type': 'earth',
                        'subtype': {
                            1: {
                                'total': 200,
                                'interval_time': 3
                            },                            
                        },
                        
                    },
                    {
                        'type': 'fly',
                        'subtype': {
                            1: {
                                'total': 120,
                                'interval_time': 4
                            },
                            2: {
                                'total': 50,
                                'interval_time': 5
                            }
                        },
                        
                    },
                    
                ]
            }, 
        }

def lvl(l):
  return levels[l]

for x in levels:
  if(x == 1):
    enemies = levels[x]['enemies']
    for e in enemies:
        for k ,v in e.items():
            print(v)


for level, level_data in levels.items():
    for enemy_data in level_data['enemies']:
        for subtype, subtype_data in enemy_data['suptye'].items():
            total = subtype_data['total']
            interval_time = subtype_data['interval_time']
