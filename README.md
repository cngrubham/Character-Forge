# CHARACTER FORGE
A PostgreSQL/Django application demonstrating use of 7 restful routes for CRUD operations,
along with utilization of external APIs for data retrieval.

### Heroku link

[Character Forge](https://character-forge-1fbe226688ee.herokuapp.com/)

### Technologies used

* Python
* PostgreSQL
* Django

### CRUD Table

![CRUD table](/main_app/static/assets/Character_Forge_CRUD_table.png "CRUD table")

### ERD Diagram

![ERD diagram](/main_app/static/assets/Character_Forge_ERD.png "ERD diagram")

### Installation Instructions

#### Run the following for setup:

* sudo apt-get install python3-pip
* pip3 install Django
* pip3 install psycopg2-binary
* createdb characterforge
* python3 manage.py makemigrations
* python3 manage.py migrate

#### Start the server

* python3 manage.py runserver

#### Make sure global .gitignore file includes the following:

**Django**

* .log
* local_settings.py
* db.sqlite3
* db.sqlite3-journal

**Python**

* .env
* *.py[cd]
* "\_\_pycache__/"
* .python-version


### User stories

* As a user, I want to create my user profile so that I can begin creating characters.
* As a user, I want to modify my user profile, as my personal details change.
* As a user, I want to delete my user profile.
* As a user, I want to see my user page and all of my characters listed.
* As a user, I want to create a character.
* As a user, I want to edit a character.
* As a user, I want to delete a character.

### Wireframes

![Home page](/main_app/static/assets/home_page.png "Home page")\
![Generic Form](/main_app/static/assets/generic_form.png "Generic Form")\
![User Form](/main_app/static/assets/user_form.png "User Form")\
![Character Form](/main_app/static/assets/character_form.png "Character Form")\
![Character Details](/main_app/static/assets/character_details.png "Character Details")

### Screenshots

![Home page](/main_app/static/assets/home_screenshot.png "Home page")\
![User Index](/main_app/static/assets/user_index_screenshot.png "User Index")\
![New User](/main_app/static/assets/create_user_screenshot.png "New User")\
![Edit User](/main_app/static/assets/edit_user_screenshot.png "Edit User")\
![User Details](/main_app/static/assets/user_detail_screenshot.png "User Details")\
![Create Character](/main_app/static/assets/create_character_screenshot.png "Create Character")\
![Character Detail](/main_app/static/assets/character_detail_screenshot.png "Character Detail")\
![Character Edit](/main_app/static/assets/character_edit_screenshot.png "Character Edit")

### Learnings

1. Integrating data from an external API into a Django template was a new learning. 
    1. Views.py
        1. Setting up a proxy URL view function.
        ```
        def proxy_api(request, alignment_name):
            # Construct the URL for the external API
            api_url = f'https://www.dnd5eapi.co/api/alignments/{alignment_name}'
        
            # Make a request to the external API
            response = request.get(api_url)
            data = response.json()
    
            return JsonResponse(data) 
        ```
       
    2. urls.py
        1. Setting up a path in the urlpatterns list.
        ```
        path('proxy_api/<str:alignment_name>/', views.proxy_api, name='proxy_api'),
        ```
    3. character_form.html
        1. JS code
        ```
        document.addEventListener("DOMContentLoaded", function() {
            const alignmentDropdown = document.querySelector("#id_alignment");
            const raceDropdown = document.querySelector("#id_race"); // Select the race dropdown
    
            alignmentDropdown.addEventListener("change", function() {
                const selectedAlignment = this.value;
                fetchAlignmentData(selectedAlignment);
            });
    
            raceDropdown.addEventListener("change", function() {
                const selectedRace = this.value;
                fetchRaceData(selectedRace);
            });
    
            function fetchAlignmentData(alignment_name) {
                console.log("Fetching alignment data...");
                alignment_name = alignment_name.toLowerCase().replace(" ", "-");
                const url = `https://www.dnd5eapi.co/api/alignments/${alignment_name}`;
    
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        const alignmentNameElement = document.querySelector("#alignment-name");
                        const alignmentDescElement = document.querySelector("#alignment-desc");
    
                        alignmentNameElement.textContent = data.name;
                        alignmentDescElement.textContent = data.desc;
                    })
                    .catch(error => {
                        console.error("Error fetching alignment data: ", error);
                    });
            }
    
            function fetchRaceData(race_name) {
                console.log("Fetching race data...");
                race_name = race_name.toLowerCase().replace(" ", "-");
                const url = `https://www.dnd5eapi.co/api/races/${race_name}`;
    
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        const raceNameElement = document.querySelector("#race-name");
                        const raceAlignElement = document.querySelector("#race-align");
                        const raceLangElement = document.querySelector("#race-lang");
                        const raceTraitsElement = document.querySelector("#race-traits");
    
                        raceNameElement.textContent = data.name;
                        raceAlignElement.textContent = data.alignment;
                        raceLangElement.textContent = data.language_desc;
                        raceTraitsElement.textContent = data.traits.name;
                        const traits = data.traits.map(trait => trait.name);
                        raceTraitsElement.textContent = traits.join(', '); // Display traits as a comma-separated list
                    })
                    .catch(error => {
                        console.error("Error fetching race data: ", error);
                    });
            }
        });
        ```
2. Learning how to take an image (20-sided dice) and add animation to it, and also adding JS events to generate values for the character attributes.
    1. style.css
    ```
    .center-align-dice {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
    }

    .rotate-center {
        animation: rotate-center 5s linear infinite both;
        margin-top: 40px;
    }

    .rotate-center:hover {
        animation-play-state: paused;
    }

    @keyframes rotate-center {
        0% {
            transform: rotate(0);
        }
    
        100% {
            transform: rotate(360deg);
        }
    }

    .spin {
        animation: rotate-center 5s linear infinite both;
        margin-top: 40px;
    }
    
    @keyframes spin {
        0% {
            transform: rotate(0);
        }
    
        100% {
            transform: rotate(360deg);
        }
    }
    ```
    2. JS script in character_form.html
    ```
    document.addEventListener("DOMContentLoaded", function () {
        function getRandomStat() {
                return Math.floor(Math.random() * 13) + 8;
        }
    
    let generateStatsButton = document.getElementById("generate-stats");

    generateStatsButton.addEventListener("click", function () {

        generateStatsButton.classList.add("spin");

        let strength = getRandomStat();
        let constitution = getRandomStat();
        let dexterity = getRandomStat();
        let charisma = getRandomStat();
        let wisdom = getRandomStat();
        let intelligence = getRandomStat();

        document.getElementById("id_strength").value = strength;
        document.getElementById("id_constitution").value = constitution;
        document.getElementById("id_dexterity").value = dexterity;
        document.getElementById("id_charisma").value = charisma;
        document.getElementById("id_wisdom").value = wisdom;
        document.getElementById("id_intelligence").value = intelligence;

        setTimeout(function () {
                generateStatsButton.classList.remove("spin");
            }, 3000);
        }); // Close generate-status event listener
    }); // Close DOMContentLoaded event listener
    ```
3. We learned how to customize a Django ModelForm so that we could add JS event listeners to the HTML elements.
    1. user_form.html
        1. HTML
        ```
        <tr>
            <td><label for="id_{{ form.avatar.name }}" class="form-label">{{ form.avatar.name|capfirst }}:</label></td>
            <td>
                <select name="{{ form.avatar.name }}" id="id_{{ form.avatar.name }}">
                    {% for choice in form.avatar.field.choices %}
                        <option value="{{choice.0}}" {% if choice.1 == form.avatar.value %}selected{% endif %}>{{ choice.1 }}</option>
                    {% endfor %}
                </select>
            </td>
        </tr> 
        ```
        2. Javascript
        ```
        <script>
    
            // This code ensures that the image for 
            // the default value is displayed upon load of the form.
            document.addEventListener("DOMContentLoaded", function() {
                const dropdown = document.getElementById('id_avatar'); 
                const selectedValue = dropdown.value;
        
                console.log(selectedValue);
        
                // Hide all images initially
                document.querySelectorAll('img').forEach(function(img) {
                    img.style.display = 'none';
                });
        
                // Show the image with the matching alt value
                const matchingImage = document.querySelector('img[alt="' + selectedValue + '"]');
                
                if (matchingImage) {
                    matchingImage.style.display = 'block';
                }
            
            });
        
            // This code changes the displayed image, 
            // based on the user selection in the dropdown.
            document.querySelector('#id_avatar').addEventListener('change', function() {
                // Get the selected value
                const selectedValue = this.value;
            
                // Hide all images initially
                document.querySelectorAll('img').forEach(function(img) {
                    img.style.display = 'none';
                });
            
                // Show the image with the matching value
                document.querySelector('img[alt="' + selectedValue + '"]').style.display = 'block';
            });
        
        </script>
        ```
4. We learned how to set up password masking for a field in a ModelForm.
    1. forms.py
    ```
    from django.forms.widgets import Select, PasswordInput
    
    class UserForm(ModelForm):
      class Meta:
        model = User
        fields = "__all__"
        widgets = {
          'avatar': Select(choices=FACTION_CHOICES),
          'password': PasswordInput(),
        }
    ```
    2. user_form.html
        1. The code below handles both new users and edit of existing users.
        ```
        <tr>
            <td><label for="id_{{ form.password.name }}" class="form-label">{{ form.password.name|capfirst }}:</label></td>
            {% if object %}
                <td><input type="password" name="{{ form.password.name }}" id="{{ form.password.id }}" value="{{ form.password.value }}"></tr></td>
            {% else %}
                <td>{{ form.password }}</td>
            {% endif %}
        </tr>
        ```