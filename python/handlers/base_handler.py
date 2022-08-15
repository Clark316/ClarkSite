from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
  
  def options(self, *args, **kwargs):
    self.set_status(200)
    self.finish()
  
  def set_default_headers(self, *args, **kwargs):
    self.set_header("Access-Control-Allow-Origin", "*")
    self.set_header("Access-Control-Allow-Headers", "access-control-allow-origin,authorization,content-type") 
    self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")