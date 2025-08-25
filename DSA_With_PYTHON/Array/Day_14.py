# product model chek
def product_model_check(products):
    """
    This function checks if the product model is valid.
    
    :param products: List of product models
    :return: True if all models are valid, False otherwise
    """
    for product in products:
        if not isinstance(product, str) or len(product) < 3:
            return False
    return True