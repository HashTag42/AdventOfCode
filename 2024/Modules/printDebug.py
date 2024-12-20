import logging

################################################################################
def printVarValue(DEBUG, var, namespace):
    if DEBUG:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        var_name = [name for name, value in namespace.items() if value is var][0]
        logging.debug(f"{var_name} = {var}")
################################################################################
