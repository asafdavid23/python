# import modules
import os
import re
import yaml
import argparse
import jinja2 as jinja
import time

# Load templates folder into jinja2 environment
file_loader = jinja.FileSystemLoader('templates')
env = jinja.Environment(loader=file_loader)

# parse config file
with open('config.yaml', 'r') as cf:
    config = yaml.load(cf, Loader=yaml.FullLoader)
    
def create_folder_structure(accounts, regions, environments, rendered_file):
    """ Create folder structure for each account, region, and environment

    Args:
        accounts (list): list of aws accounts
        regions (list): lisr of aws regions
        environments (list): list of environments
        rendered_file (str): rendered file from jinja2
    """
    if not os.path.exists('./live'):
        os.mkdir('live')
        os.popen(f'cd live && touch .terraform-version .terragrunt-version')
        f = open('live/terragrunt.hcl', 'a')
        f.write(rendered_file)
        f.close
        for account in accounts:
            os.popen(f'cd live && mkdir {account} && touch {account}/account.yaml')
            time.sleep(2)
            for region in regions:
                os.popen(f'cd live/{account} && mkdir {region} && touch {region}/region.yaml')
                time.sleep(2)
                for environment in environments:
                    os.popen(f"cd live/{account}/{region} && mkdir {environment} && touch {environment}/env.yaml")
    else:
        for account in accounts:
            if not os.path.exists(f'live/{account}'):
                os.popen(f'cd live && mkdir {account} && touch {account}/account.yaml')
                time.sleep(2)
                for region in regions:
                    if not os.path.exists(f'live/{account}/{region}'):
                        os.popen(f'cd live/{account} && mkdir {region} && touch {region}/region.yaml')
                        time.sleep(2)
                        for environment in environments:
                            if not os.path.exists(f'live/{account}/{region}/{environment}'):
                                os.popen(f"cd live/{account}/{region} && mkdir {environment} && touch {environment}/env.yaml")

def render_file(template, config):
    """ Render file using jinja2

    Args:
        template (str): string of jinja2 template
        config (dict): config dictionary

    Returns:
        str: rendered file from jinja2
    """
    tmp = env.get_template(template)
    tmp = tmp.render(
        state_s3_bucket = config['terrgrunt']['s3_backend_config']['bucket'],
        state_s3_bucket_region = config['terrgrunt']['s3_backend_config']['region'],
        package_name = config['terrgrunt']['package_name'],
        state_s3_lock_table = config['terrgrunt']['s3_backend_config']['dynamodb_table']
    )
    return tmp

rendered_file = render_file('parrent.hcl.jinja', config)
create_folder_structure(config['accounts'], config['regions'], config['environments'], rendered_file)

