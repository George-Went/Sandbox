from application.extensions import db

# Containers Model 
class Container(db.Model):
    __tablename__ = 'containers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    image = db.Column(db.String, nullable=False)
    command = db.Column(db.String)
    entrypoint = db.Column(db.String)
    environment = db.Column(db.String)
    network = db.Column(db.String)
    network_mode = db.Column(db.String)
    ports = db.Column(db.String)
    restart_policy = db.Column(db.String)
    volumes = db.Column(db.String)

    def __repr__(self):
        return f"Post('{self.id}','{self.name}','{self.image}','{self.command}','{self.entrypoint}','{self.environment}','{self.network}','{self.network_mode}','{self.ports}','{self.restart_policy}','{self.volumes}')"

