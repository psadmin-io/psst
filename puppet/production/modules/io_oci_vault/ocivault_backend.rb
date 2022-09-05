class Hiera
    module Backend
      class Ocivault_backend
  
        def initialize
          Hiera.debug("Hiera OCI Vault backend starting")
        end
  
        def lookup(key, scope, order_override, resolution_type)
          answer = nil
          return if key.start_with?('ocivault::') == false
  
          secret = key.dup
          secret.slice! "ocivault::"
  
          Hiera.debug("Looking up #{key} in OCI Vault backend")
  
          oci_vault_ocid = Facter.value(:oci_vault_ocid)
          Hiera.debug("OCI Value OCID: #{oci_vault_ocid}")
  
          ocicli = `oci secrets secret-bundle get-secret-bundle-by-name \
                      --vault-id=#{oci_vault_ocid} \
                      --secret-name=#{secret} \
                      --auth instance_principal \
                      | jq -jr '.data."secret-bundle-content".content' \
                      2>/dev/null `
          ocicli = Base64.decode64(ocicli)
          return if ocicli.empty?
  
          Hiera.debug("Found #{key} in OCI Vault")
          answer = Backend.parse_answer(ocicli, scope, {})
  
          return answer
        end
      end
    end
  end