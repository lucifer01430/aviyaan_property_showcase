from django.utils.deprecation import MiddlewareMixin
import time
import random

class DeveloperConsoleMiddleware(MiddlewareMixin):

    ENABLE_ON_LOCALHOST = True

    ENCODED_JS = (
        "Y29uc29sZS5sb2coCiAgJyVjRGVzaWduICYgRGV2ZWxvcGVkIGJ5IEhhcnNoIFBhbmRleScs"
        "CiAgJ2NvbG9yOiMwMGU2NzY7IGZvbnQtc2l6ZToxNHB4OyBmb250LXdlaWdodDo2MDA7Jwop"
        "Owpjb25zb2xlLmxvZygKICAnJWNXZWIgRGV2ZWxvcGVyXG5Qb3J0Zm9saW86IGh0dHBzOi8v"
        "bHVjaWZlcjAxNDMwLmdpdGh1Yi5pby9Qb3J0Zm9saW8nLAogICdjb2xvcjojOWU5ZTllOyBm"
        "b250LXNpemU6MTJweDsnCik7Cg=="
    )

    def process_response(self, request, response):
        content_type = response.get("Content-Type", "")


        if "text/html" not in content_type:
            return response


        if not self.ENABLE_ON_LOCALHOST:
            host = request.get_host()
            if host.startswith(("127.0.0.1", "localhost")):
                return response


        if b"</body>" not in response.content:
            return response


        vm_name = "VM" + str(int(time.time() * 1000) + random.randint(1, 999))[-4:]

        script = f"""
<script>
(function(){{
  try {{
    var encoded = "{self.ENCODED_JS}";
    eval(atob(encoded) + "\\n//# sourceURL={vm_name}");
  }} catch(e) {{}}
}})();
</script>
""".encode("utf-8")

        response.content = response.content.replace(
            b"</body>",
            script + b"</body>"
        )

        return response
