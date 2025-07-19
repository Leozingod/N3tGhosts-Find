import requests

site = input("Digite o site (ex: https://exemplo.com): ").strip()
if site.endswith("/"):
    site = site[:-1]

caminhos = [
    "admin", "administrator", "admin1", "admin2", "admin3", "admin_area", "admin_area_login",
    "admin_backup", "admin_control", "admin_control_panel", "admin_cp", "admin_dashboard",
    "admin_dev", "admin_index", "admin_login", "admin_login_page", "admin_panel", "admin_panel_login",
    "admin_portal", "admin_site", "admin_site_login", "admin_system", "admin_user", "admin_users",
    "adminportal", "adminpanel", "adminpanel_area", "adminpanelcp", "adminpanel_login", "admincp",
    "admincpanel", "adminconsole", "adminconsole_login", "adm", "adm_area", "adm_login", "admcp",
    "admcpanel", "admcpanel_login", "admlogin", "admin-login", "admin-login_page", "admin-loginpanel",
    "admin-login-user", "admin_login_area", "admin_login_form", "admin_login_page", "adminlogin",
    "adminloginpage", "adminlogins", "adminloginarea", "adminarea", "adminarea_login", "adminarea_users",
    "adminroot", "adminuser", "adminusers", "adminweb", "adminsite", "adminhome", "admindashboard",
    "admindashboard_area", "adminaccess", "adminaccess_login", "admzone", "adminzone_login",
    "superadmin", "superadmin_login", "login", "loginadmin", "login_panel", "login_area",
    "login_user", "loginusers", "userlogin", "user_admin", "user_area", "user_panel", "userloginarea",
    "painel", "painel_admin", "painel_de_controle", "painel_restrito", "painel_login",
    "paineladm", "paineladm_login", "painelusuario", "paineluser", "painelusers", "cpanel",
    "cpanel_login", "controle", "controle_admin", "controle_de_acesso", "controle_login",
    "dashboard", "dashboard_admin", "dashboard_login", "backend", "backend_admin", "backend_login",
    "root", "root_login", "manager", "manager_login", "staff", "staff_login", "portal",
    "portal_admin", "portal_login", "secure", "secure_admin", "secure_login", "siteadmin",
    "siteadmin_login", "sitecontrol", "sitecontrol_login", "webadmin", "webadmin_login",
    "webpanel", "webpanel_login", "admin_console", "admin_console_login", "access", "access_login",
    "restricted", "restricted_area", "restricted_login", "adm_area_login", "administracao",
    "administrador", "administração_login", "administration", "administration_login", "sysadmin",
    "sysadmin_login", "system_admin", "system_admin_login", "adm_login_area", "adm_login_form",
    "adm_login_page", "admin_center", "admin_center_login", "admin_home", "admin_home_login",
    "adm_user", "adm_users", "admzone_area", "admzone_panel", "admzone_login", "admzone_admin",
    "administrator_area", "administrator_panel", "administrator_login", "adminpanel_area",
    "adminpanel_login", "adminpanel_users", "admincp_area", "admincp_login", "admcp_area",
    "admcp_login", "admconsole_area", "admconsole_login", "adminaccess_area", "adminaccess_login",
    "adminuser_area", "adminuser_login", "adminusers_area", "adminusers_login", "superadmin_area",
    "superadmin_panel", "superadmin_login", "controlpanel", "controlpanel_login", "controlpanel_admin",
    "adminconsole_panel", "adminconsole_login", "admcpanel_area", "admcpanel_login", "admzone_panel",
    "admzone_login", "adminroot_panel", "adminroot_login", "adminlogin_area", "adminlogin_panel",
    "adminlogin_login", "admininterface", "admin_interface_login", "adminportal_area",
    "adminportal_login", "adminportal_panel", "admindashboard_login", "admindashboard_panel",
    "adminsystem", "adminsystem_login", "adminsystem_panel", "adminsite_area", "adminsite_login",
    "adminsite_panel", "admincontrol", "admincontrol_login", "admincontrol_panel", "adminpage",
    "adminpage_login", "adminpage_panel", "adminlogin_page", "adminlogin_form", "adminlogin_area",
    "adminpanel_page", "adminpanel_form", "adminpanel_area", "adminpanel_login", "adminpanel_user",
    "adminpanel_users", "adminuser_panel", "adminuser_login", "adminusers_panel", "adminusers_login",
    "admindashboard_user", "admindashboard_users", "admincontrol_user", "admincontrol_users",
    "adminaccess_user", "adminaccess_users", "admconsole_user", "admconsole_users", "admcp_user",
    "admcp_users", "admcpanel_user", "admcpanel_users", "admzone_user", "admzone_users", "adminroot_user",
    "adminroot_users", "adminlogin_user", "adminlogin_users", "admininterface_user", "admininterface_users",
    "adminportal_user", "adminportal_users", "adminsystem_user", "adminsystem_users", "adminsite_user",
    "adminsite_users", "admincontrol_user", "admincontrol_users", "adminpage_user", "adminpage_users",
    "adminloginuser", "adminloginusers", "adminpaneluser", "adminpanelusers", "admindashboarduser",
    "admindashboardusers", "admincontroluser", "admincontrolusers", "adminaccessuser", "adminaccessusers",
    "admconsoleuser", "admconsoleusers", "admcpuser", "admcpusers", "admcpaneluser", "admcpanelusers",
    "admzoneuser", "admzoneusers", "adminrootuser", "adminrootusers", "adminloginuser", "adminloginusers"
]

print("\n🔎 Iniciando busca por painéis de admin...\n")

for caminho in caminhos:
    url = f"{site}/{caminho}"
    try:
        resposta = requests.get(url, timeout=5)
        print(f"Url: {url} - Status: {resposta.status_code}")
        if resposta.status_code == 200:
            print(f"\n✅ Painel encontrado: {url}")
            break
    except requests.exceptions.RequestException:
        print(f"Url: {url} - Erro ao acessar")
        continue
else:
    print("\n🔚 Nenhum painel encontrado.")

print("\n🔒 Busca finalizada.")
