
from .access_pwd import generate
from .db_user_pwd import generate
from .db_admin_pwd import generate
from .pskey_password import generate
from .db_connect_pwd import generate
from .domain_conn_pwd import generate
from .wls_admin_user_pwd import generate
from .pia_gateway_admin_pwd import generate
from .pia_webprofile_user_pwd import generate
from .es_admin_pwd import generate
from .es_proxy_pwd import generate
from .windows_password import generate

# TODO - need to review these
  #         secrets.append("connect_pwd")
    #         secrets.append("access_pwd")
    #         secrets.append("admin_pwd")
    #         secrets.append("weblogic_admin_pwd")
    #         secrets.append("webprofile_user_pwd")
    #         secrets.append("gw_user_pwd")
    #         secrets.append("domain_conn_pwd")
    #         secrets.append("opr_pwd")
    #         secrets.append("db_admin_pwd")