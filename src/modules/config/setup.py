class SetUpExecuter():
    """
    Attributes
    ---
    """
    filepath = "..\\..\\config\\defaults.yaml" # default filepath for configuration
    venv_prefix = "python" #prefix for operations (not currently using venv, but can be done)
    os = __import__('os') # os module as attribute
    log = __import__('logging') #logging module as attribute
    """
    Methods
    ---
    """
    def __init__(self):
        """
        Function that initializes class
        Params: No arguments/parameters
        Objective: Setup is invoked at the creation of the class, logs about the installments is also created.
        """
        import logging
        logFileFormatter = logging.Formatter(
            fmt=f"%(levelname)s %(asctime)s (%(relativeCreated)d) \t %(pathname)s F%(funcName)s L%(lineno)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        fileHandler = logging.FileHandler(filename='installments.log') #output file for logs
        fileHandler.setFormatter(logFileFormatter)
        fileHandler.setLevel(level=logging.INFO)
        logging.basicConfig(level=logging.INFO)
        self.log = logging.getLogger(__name__) #<<<<<<<<<<<<<<<<<<<<
        self.log.addHandler(fileHandler)

        self.read_defaults()
        self.install_test_modules()
        self.install_services()

    def install_services(self)->None:
        """
        Class method
        ---
        Params: No arguments/parameters
        Objective: Install recursively the listed modules in YAML into python environment
        """
        print("Checking in to api-connection and app installations...")

        for module in self.yaml_config["python"]["global"]["modules"]["standard"]:
            try:
                self.log.info("Checking {} module into venv".format(module["import"]))
                assert __import__(module["import"])
            except ImportError as error:
                self.log.info("Installing {} module into venv".format(module["install"]))
                self.os.system("{} pip install {}".format(self.venv_prefix, module["install"]))

    def install_test_modules(self)->None:
        """
        Class method
        ---
        Params: No arguments/parameters
        Objective: Install the mentioned module into python environment
        """
        self.log.info("Checking in to services installation...")

        import sys

        module_ = 'pytest-virtualenv' #pytest for virtual environments

        if module_ in sys.modules:
            self.log.info("Checking {} module into venv".format(module_))
        else:
            self.log.info("Installing {} module into venv".format(module_))
            self.os.system("{} pip install {}".format(self.venv_prefix, module_))    

        for module in self.yaml_config["python"]["global"]["modules"]["test"]:
            try:
                self.log.info("Checking {} module into venv".format(module["import"]))
                assert __import__(module["import"])
            except ImportError as error:
                self.log.info("Installing {} module into venv".format(module["install"]))
                self.os.system("{} pip install {}".format(self.venv_prefix, module["install"]))

    def read_defaults(self)->None:
        """
        Class method
        ---
        Params: No arguments/parameters
        Objective: Read YAML file and set information in attribute
        """
        fullpath = self.os.path.join(self.os.path.dirname(__file__), self.filepath)

        try:
            self.log.info("Checking {} module into venv".format("yaml"))
            assert __import__("yaml")
        except ImportError as error:
            self.log.info("Installing {} module into venv".format("PyYaml"))
            self.os.system("{} pip install {}".format(self.venv_prefix,"pyyaml"))
        finally:
            yaml = __import__("yaml")
        
        self.log.info("Reading configuration variables on YAML...")
        with open(fullpath, 'r') as file:
            self.yaml_config = yaml.safe_load(file)