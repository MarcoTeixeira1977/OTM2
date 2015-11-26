from optparse import make_option

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Creates a new User Defined Field (UDF)'

    option_list = BaseCommand.option_list + (
        make_option('--name',
                    dest='name',
                    help='Specify field name'),
        make_option('--type',
                    dest='type',
                    help='Either Plot or Tree'),
        make_option('--iscollection',
                    dest='iscollection',
                    help='Only Non-Collections are currently supported by this utility.'),
        make_option('--choices',
                    dest='choices',
                    help='Comma delimited list.'),
        )

    # ToDo: ensure type is in ("Tree", "Plot")
    def handle(self, *args, **options)
        new_udf = UserDefinedFieldDefinition(
                name=options["name"],
                model_type=options["model_type"],
                iscollection=options["iscollection"],
                datatype="""{{
                  "type": "{thetype}",
                  "choices": {choices},
                  "description": {description}"
                  }}""".format(thetype=options["type"],
                               choices=choices,
                               description=description)
                  )
        new_udf.save()
        # Default permissions are "Invisible"
        # Changing to Full Write # ToDo: parameterize the permissions for each user type
        for ausers_perms in FieldPermission.objects.filter(field_name="udf:{}".format(options["name"])):
            ausers_perms.permission_level=3
            ausers_perms.save()
