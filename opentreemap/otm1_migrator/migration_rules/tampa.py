# 
from otm1_migrator.migration_rules.standard_otm1 import MIGRATION_RULES

from treemap.models import ITreeCodeOverride, ITreeRegion, User

UDFS = {
    'plot': {
        'owner_additional_id': {
            'udf.name': 'Owner Additional Id'
        },
        'owner_additional_properties': {
            'udf.name': 'Owner Additional Properties'
        },
        'type': {
            'udf.name': 'Plot Type',
            'udf.choices': ['Well/Pit', 'Median/Island', 'Tree Lawn',
                            'Park', 'Planter', 'Other', 'Yard',
                            'Natural Area']
        },
        'powerline_conflict_potential': {
            'udf.name': 'Powerlines Overhead',
            'udf.choices': ['Yes', 'No', 'Unknown']
        },
        'Sidewalk Damage': {
            'udf.name': 'Sidewalk Damage',
            'udf.choices': ['Minor or No Damage', 'Raised More Than 3/4 Inch']
        }
    },
    'tree': {
        'sponsor': {'udf.name': 'Sponsor'},
        'projects': {'udf.name': 'Projects'},
        'canopy_condition': {
            'udf.name': 'Canopy Condition',
            'udf.choices': ['Full - No Gaps',
                            'Small Gaps (up to 25% missing)',
                            'Moderate Gaps (up to 50% missing)',
                            'Large Gaps (up to 75% missing)',
                            'Little or None (up to 100% missing)']
        },
        'condition': {
            'udf.name': 'Tree Condition',
            'udf.choices': ['Dead', 'Critical', 'Poor',
                            'Fair', 'Good',
                            'Very Good', 'Excellent']
        }
    }
}

#SORT_ORDER_INDEX = {
#}



#MIGRATION_RULES['species']['postsave_actions'] = (MIGRATION_RULES['species']
#                                                  .get('postsave_actions', [])
#                                                  + [create_override])



# Species
MIGRATION_RULES['species']['removed_fields'].remove('family')
MIGRATION_RULES['species']['common_fields'].remove('other_part_of_name')
MIGRATION_RULES['species']['missing_fields'].add('other_part_of_name')

# Plot
MIGRATION_RULES['plot']['removed_fields'].remove('powerline_conflict_potential')
MIGRATION_RULES['plot']['common_fields'].add('powerline_conflict_potential')
MIGRATION_RULES['plot']['sidewalk_damage'].remove('powerline_conflict_potential')
MIGRATION_RULES['plot']['sidewalk_damage'].add('powerline_conflict_potential')
# Tree
MIGRATION_RULES['tree']['renamed_fields']['id']='cota_id'
MIGRATION_RULES['tree']['common_fields'].add('canopy_condition')
MIGRATION_RULES['tree']['removed_fields'].remove('canopy_condition')

#MIGRATION_RULES['tree']['removed_fields'].remove('pests')
#MIGRATION_RULES['tree']['removed_fields'].remove('url')

#MIGRATION_RULES['boundary']['presave_actions'] = (MIGRATION_RULES['boundary']
#                                                  .get('presave_actions', [])
#                                                  + [mutate_boundary])
#MIGRATION_RULES['species']['missing_fields'] |= {'other'}

# these fields don't exist in the ptm fixture, so can't be specified
# as a value that gets discarded. Remove them.
#MIGRATION_RULES['species']['removed_fields'] -= {'family'}
#MIGRATION_RULES['tree']['removed_fields'] -= {'pests', 'url'}

# this field doesn't exist, so can no longer have a to -> from def
#del MIGRATION_RULES['species']['renamed_fields']['other_part_of_name']
#MIGRATION_RULES['species']['common_fields'].remove('other_part_of_name')
