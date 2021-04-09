PakistanX XYZ
---------------------------------------------

This XBlock allows Learners to  

Installation
------------

Install the requirements into the python virtual environment of your
``edx-platform`` installation by running the following command from the
root folder:

    pip install -e git@github.com:PakistanX/pakx-xyz-xblock.git@release-v0.1.0#egg=pakx_xyz

Enabling in Studio
------------------

You can enable the PakX XYZ XBlock in studio through the
advanced settings.

1. From the main page of a specific course, navigate to
   `Settings -> Advanced Settings` from the top menu.
2. Check for the ``advanced_modules`` policy key, and add
   ``"pakx_xyz"``.
3. Click the `"Save changes"` button.


Usage
-----

The PakistanX XYZ .... Add the PakistanX XYZ 
component to a lesson, then click the `EDIT` button.

![Studio View](/doc/imgs/studio-view.png)

Details here


![LMS View](/doc/imgs/lms-view.png)

Details here

Running the workbench
---------------------
`python manage.py runserver 8000`

Access it at 

`http://localhost:8000/` <http://localhost:8000>.
