################################################################################
def printDebug(var, namespace):
    var_name = [name for name, value in namespace.items() if value is var][0]
    print(f"[DEBUG] {var_name} = {var}")
################################################################################
