import json
import configparser

class Config:
    def __init__(self, file_path):
        
        # Store the file path of the config file
        
        self.file_path = file_path
        
        # Initialize the config property as an empty list
        
        self.config = []
        self.format = None
        
        # Determine the format of the config file based on the file extension
        
        if self.file_path.endswith('.json'):
            self.format = 'json'
        elif self.file_path.endswith('.conf'):
            self.format = 'ini'
        else:
            raise ValueError('Unsupported file format')

    def load(self):
        
        # Load the config file based on its format
        
        if self.format == 'json':
            
            # Read the JSON file and store its contents in the config property
            
            with open(self.file_path, 'r') as f:
                self.config = json.load(f)
        elif self.format == 'ini':
            
            # Read the INI file using the ConfigParser library
            
            config_parser = configparser.ConfigParser()
            config_parser.read(self.file_path)
            
            # Convert each section of the INI file into a dictionary and add it to the config list
            
            for section in config_parser.sections():
                self.config.append({section: dict(config_parser[section])})
                
        return self.config

    def save(self, config=None):
        
        # If a new config is passed as an argument, store it in the config property
        
        if config:
            self.config = config
            
        # Save the config file based on its format
        
        if self.format == 'json':
            
            # Write the config to a JSON file
            
            with open(self.file_path, 'w') as f:
                json.dump(self.config, f)
        elif self.format == 'ini':
            
            # Write the config to an INI file using the ConfigParser library
            
            config_parser = configparser.ConfigParser()
            
            # Loop through each dictionary in the config list and add it as a section to the ConfigParser object
            
            for config_section in self.config:
                section = list(config_section.keys())[0]
                config_parser[section] = config_section[section]
                
            # Write the ConfigParser object to an INI file
            
            with open(self.file_path, 'w') as f:
                config_parser.write(f)