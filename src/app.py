from flask import Flask
from flask_graphql import GraphQLView

from models import db_session
from schema import schema

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

# TEMP
# Base.metadata.create_all(bind=engine)

# engineering = Department(name='Engineering')
# db_session.add(engineering)
# hr = Department(name='Human Resources')
# db_session.add(hr)

# peter = Employee(name='Peter', department=engineering)
# db_session.add(peter)
# roy = Employee(name='Roy', department=engineering)
# db_session.add(roy)
# tracy = Employee(name='Tracy', department=hr)
# db_session.add(tracy)
# db_session.commit()
# TEMP

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
