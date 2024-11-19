def parse_threat_data(raw_data):
    parsed = {"ip": raw_data.get("ip", ""), "malicious": raw_data.get("malicious", False)}
    return parsed