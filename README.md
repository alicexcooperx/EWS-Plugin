# EWS-Plugin
This repo contains the code to do the following functions:

A. Parse the ticket and create a DTO Object.

B. Sanitise the attachments, and description of the ticket.

C. Redact any sensitive information from the ticket.

# Redaction
Please download Bulk_Extractor first before you use this program from: https://github.com/simsong/bulk_extractor

When implementing the Redaction you need to make sure that you set

parent_dir = r"C:\\Users\\test\\test\\" <- to your folder which the BE output files will go. 

# Sanitization 
Make sure you have a VirusTotal account before you use this program. NOTE: you will only be limited to 4 requests per minute. (unless you have a premium key)

You also need to make sure you have a directory which includes all the attachments you are going to feed into the program:

command = 'bulk_extractor -S ssn_mode=2 -o "' + self.full_directory_path + '" -R "C:\\Users\\test\\test"' <- Folder which includes the attachments you want to scan and redact

# NOTE: This program does not support PDF, ZIP or GZIP currently.
