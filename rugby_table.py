from app import app, db
from app.models import Team, Stats, Round


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Team': Team, 'Stats': Stats, 'Round': Round}
