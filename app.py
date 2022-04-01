from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    title = "Welcome to conference"
    return render_template('home.html',title=title)

@app.route('/aboutus')
def about_us():
    title = "About Us"
    return render_template('aboutus.html',title=title)

@app.route('/hotels')
def hotels():
    title = "Hotels and Travels"
    return render_template('hotel.html',title=title)

@app.route('/registration')
def registration():
    title = "Registration"
    return render_template('registration.html',title=title)

@app.route('/sponsors')
def sponsors():
    title = "Sponsorships"
    return render_template('sponsors.html',title=title)

######################### ROUTES FOR MEMBERS ###################################3
@app.route('/all-chairs')
def all_chairs():
    title = "All members"
    return render_template('all_chairs.html',title=title)

@app.route('/workshop-chairs')
def workshop_chairs():
    title = "Workshops / Tracks Chair"
    members_type_page="members/workshop_chairs.html"
    return render_template('typed_chairs.html',title=title,members_type_page=members_type_page)


@app.route('/web-chairs')
def web_chairs():
    title = "Web Chairs"
    members_type_page="members/web_chairs.html"
    return render_template('typed_chairs.html',title=title,members_type_page=members_type_page)

@app.route('/tutorials-chairs')
def tutorial_chairs():
    title = "Tutorial Chairs"
    members_type_page="members/tutorial_chairs.html"
    return render_template('typed_chairs.html',title=title,members_type_page=members_type_page)

@app.route('/sponsor-exhibition-chairs')
def sponsor_exhibition_chairs():
    title = "Sponsorship and Exhibition Members"
    members_type_page="members/sponsor_and_exhibition_chairs.html"
    return render_template('typed_chairs.html',title=title,members_type_page=members_type_page)

@app.route('/publicity-social-media-chairs')
def publicity_social_media_chairs():
    title = "Publicity and Social Media Members"
    members_type_page="members/publicity_social_media_chairs.html"
    return render_template('typed_chairs.html',title=title,members_type_page=members_type_page)

@app.route('/publications-chairs')
def publications_chairs():
    title = "Publications Members"
    members_type_page="members/publications_chairs.html"
    return render_template('typed_chairs.html',title=title,members_type_page=members_type_page)

@app.route('/program-committee-chairs')
def program_committee_chairs():
    title = "Program Committee Members"
    members_type_page="members/program_committee_chairs.html"
    return render_template('typed_chairs.html',title=title,members_type_page=members_type_page)

@app.route('/phd-track-chairs')
def phd_track_chairs():
    title = "Phd Track Chair Members"
    members_type_page="members/phd_track_chairs.html"
    return render_template('typed_chairs.html',title=title,members_type_page=members_type_page)

@app.route('/panel-chairs')
def panel_chairs():
    title = "Local Members"
    members_type_page="members/panel_chairs.html"
    return render_template('typed_chairs.html',title=title,members_type_page=members_type_page)

@app.route('/local-chairs')
def local_chairs():
    title = "Local Members"
    members_type_page="members/local_chairs.html"
    return render_template('typed_chairs.html',title=title,members_type_page=members_type_page)

@app.route('/international-chairs')
def international_chairs():
    title = "International Members"
    members_type_page="members/international_chairs.html"
    return render_template('typed_chairs.html',title=title,members_type_page=members_type_page)

@app.route('/demos-chairs')
def demos_chairs():
    title = "Demos Members"
    members_type_page="members/demos_chairs.html"
    return render_template('typed_chairs.html',title=title,members_type_page=members_type_page)

@app.route('/award-chairs')
def award_chairs():
    title = "Award Members"
    members_type_page="members/award_chairs.html"
    return render_template('typed_chairs.html',title=title,members_type_page=members_type_page)

@app.route('/general-chairs')
def general_chairs():
    title = "General Members"
    members_type_page="members/general_chairs.html"
    return render_template('typed_chairs.html',title=title,members_type_page=members_type_page)

@app.route('/technical-chairs')
def technical_chairs():
    title = "Technical Program Chairs"
    members_type_page="members/technical_chairs.html"
    return render_template('typed_chairs.html',title=title,members_type_page=members_type_page)

if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)