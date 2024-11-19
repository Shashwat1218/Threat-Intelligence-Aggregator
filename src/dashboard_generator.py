def generate_dashboard(threats):
    """
    Generates a simple dashboard displaying threat information.

    Args:
        threats (list of dict): List of threats with IP and score.

    Prints:
        Formatted threat details.
    """
    print("Threat Dashboard")
    print("-" * 30)
    for threat in threats:
        print(f"IP: {threat['ip']} - Score: {threat['score']}")