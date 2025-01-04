class Solution:
    def validIPAddress(self, IP: str) -> str:
        digits = "(25[0-5]|2[0-4]\d|1\d{0,2}|[1-9]\d|0)"
        an = "([A-F]|[a-f]|[0-9]){1,4}"
        reg_4 = re.match(r"^(%s\.){3}%s$" % (digits, digits), IP)
        reg_6 = re.match(r"^(%s:){7}%s$" % (an, an), IP)
        
        if reg_4:
            return "IPv4"
        elif reg_6:
            return "IPv6"
        else:
            return "Neither"
