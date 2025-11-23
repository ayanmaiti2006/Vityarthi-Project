
# ----- Load APK -----
def load_apk(file_path):
    try:
        apk = APK(file_path)
        return apk
    except:
        print("Error: Unable to read APK file.")
        return None

# ----- Extract Basic App Info -----
def extract_info(apk):
    print("\n--- Basic App Information ---")
    print("App Name:", apk.get_app_name())
    print("Package Name:", apk.get_package())
    print("Version:", apk.get_androidversion_name())
    print("Developer (Certificate):", apk.get_signature_names())

# ----- Dangerous Permissions -----
dangerous_permissions = [
    "READ_SMS", "SEND_SMS", "RECEIVE_SMS",
    "READ_CONTACTS", "WRITE_CONTACTS",
    "READ_CALL_LOG", "WRITE_CALL_LOG",
    "READ_PHONE_STATE",
    "SYSTEM_ALERT_WINDOW",
    "BIND_ACCESSIBILITY_SERVICE",
    "READ_EXTERNAL_STORAGE", "WRITE_EXTERNAL_STORAGE",
    "RECORD_AUDIO",
    "CAMERA"
]

def check_permissions(apk):
    print("\n--- Permission Analysis ---")
    perms = apk.get_permissions()

    suspicious = []
    for perm in perms:
        for danger in dangerous_permissions:
            if danger in perm:
                suspicious.append(perm)

    print("Total Permissions:", len(perms))
    print("Dangerous Permissions Found:")
    for s in suspicious:
        print(" -", s)

    return len(suspicious)

# ----- Developer Verification (Simple) -----
# You can add official signatures here
official_banks = {
    "com.sbi.SBIPay": "SBI",
    "com.hdfc.mobilebanking": "HDFC Bank",
    "com.icicibank.imobile": "ICICI Bank"
}

def verify_developer(apk):
    print("\n--- Developer Verification ---")
    pkg = apk.get_package()

    if pkg in official_banks:
        print("Official App:", official_banks[pkg])
        return True
    else:
        print("Warning: Package does NOT match any known official banking app.")
        return False

# ----- Risk Score Calculation -----
def calculate_risk(dangerous_count, verified):
    print("\n--- Final Risk Assessment ---")

    score = 0

    # Dangerous permissions
    if dangerous_count > 5:
        score += 2
    elif dangerous_count > 0:
        score += 1

    # Developer mismatch
    if not verified:
        score += 2

    if score >= 3:
        result = "HIGH RISK – Likely Fake"
    elif score == 2:
        result = "MEDIUM RISK – Suspicious"
    else:
        result = "LOW RISK – Likely Safe"

    print("Risk Score:", score)
    print("Verdict:", result)

# ----- Main Execution -----
file_path = "your_apk_file.apk"   # Replace with your APK path
apk = load_apk(file_path)

if apk:
    extract_info(apk)
    danger_count = check_permissions(apk)
    verified = verify_developer(apk)
    calculate_risk(danger_count, verified)