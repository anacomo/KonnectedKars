# Konnected Kars 🚔🚖🚑🚗🚜
### IoT Project

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Componenta echipei:
- Alexandra Nanu 💫
- Ana Comorasu 👩🏼‍💻
- Andrei Arnautu 🏁
- Florian Usurelu 🧚🏼‍♀️
- Vlad Ciorica 🏎


## Evaluare
### Programul trebuie să respecte următoarele cerințe (2.5p):
- [X] Expune un Rest API HTTP – documentat folosind Open API (Swagger) 
- [X] Expune un API MQTT – documentat folosind AsyncAPI
- [X] Aplicația să aibă minim 5 funcționalități – puteți să vă gândiți la ele ca sell points ale aplicației. Depinde de aplicația pe care v-ați propus să o faceți, dar chestii de genul o funcționalitate e scăderea, o altă funcționalitate e adunarea, nu înseamnă chiar că sunt diferite 
- [X] Tot ce faceți să se găsească într-un singur repo.
Pentru puncte:
- [X] Toate funcționalitățile și/sau toate endpoints au unit teste asociate. +1.5p
- [X] Documentația de analiză este up to date + 1p
- [X] Documentația de utilizare reflectă aplicația reală + 1p

### Programul trebuie să respecte următoarele cerințe:
- [X] Să prelucreze date reale (fie că accesează un alt api pentru a prelua date, fie că descărcați un set de date pe care îl dați apoi aplicației) + 1p
- [X] Utilizarea unui tool de testare automată (gen RESTler) pentru a identifica buguri. +1.5p
- [X] Integration tests +1p
- [X] Coverage al testelor de 80%+ 0.5p

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/anacomo/KonnectedKars">
    <img src="Tesla.jpg" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Konnected Kar</h3>

  <p align="center">
    An IoT program for a smart car. 
    <br />
    <a href="https://docs.google.com/document/d/1KAUPDgKP9HX05E-WcbNuEB-YcaE1hYZ6anU2qhdzbmM/edit"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <p>
    <a href="https://github.com/anacomo/KonnectedKars/issues">Report Issue</a>
    ·
    <a href="https://github.com/anacomo/KonnectedKars/issues?q=is%3Aissue+is%3Aclosed">Reopen Issue</a>
  </p>
  <br/>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#analysis-document">Analisys document</a></li>
        <li><a href="#interpretation-and-prioritization-of-requirements">Interpretation and prioritization of requirements</a> </li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#run-the-project">Run the project</a></li>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

"Konnected Kars" enables its drivers to experience first-rate driving assistance tools that guarantee safe and enjoyable rides . It's not just a product, it's a lifestyle that helps drivers to keep up with the challenges of modern times. Worn out after a day in the rat race at work? No need to worry, our smart car has got you covered. Want to impress the girl of your dreams with a romantic urban gateaway? Count on us. Driving has never been more pleasant. Konnected Kars.inc

### Built With

Major frameworks/libraries used to bootstrap KonnectedKars project:

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Python](https://www.python.org/)

### Analysis document
Visit it [here.](https://docs.google.com/document/d/1KAUPDgKP9HX05E-WcbNuEB-YcaE1hYZ6anU2qhdzbmM/edit)

### Interpretation and prioritization of requirements
* [labels & grouping](https://github.com/anacomo/KonnectedKars/issues)
* [planning poker & MoSCoW Prioritization](https://github.com/anacomo/KonnectedKars/projects/2)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Set up KonnectedKar locally:

### Prerequisites

*  Python v 3.6 or higher
* Flask
  ```sh
  pip install Flask
  ```

### Installation

1. Clone the repo
   ```sh
   git clone git@github.com:anacomo/KonnectedKars.git
2. Install flask & python packages
   ```sh
   pip install -e
   ```

### Run the project
From root directory type in a terminal:
* Windows/Linux/MacOS:
```shell script
python3 /brain/receiver.py
python3 app.py
pythn3 /sensors/runner.py
```
<p align="right">(<a href="#top">back to top</a>)</p>

### Sensors

1. Weight sensor
    ```shell script
    POST http://127.0.0.1:8000/weight_sensor
    ```

2. Distance sensor 
    ```shell script
   POST http://127.0.0.1:8000/speed_distance_sensor
    ```

3. Crash Sensor: 
    ```shell script
    POST http://127.0.0.1:8000/crash_sensor
    ```
   
4. Light Sensor:
    ```shell script 
    POST http://127.0.0.1:8000/light_sensor
   ```

5. Mist Sensor
    ```shell script
   POST http://127.0.0.1:8000/demisting_sensor
   ```

6. Enjoy our _KonnectedKars_ api - for safer, easier and the more luxurious experience while driving. 

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Determine and record environment conditions
     - [x] Record light coefficient
     - [x] Record mist coefficient
     - [x] Record distance to closest object
     - [x] Record curret speed
     - [X] Determine speed needed to avoid crashing
      
- [x] Start demisting mechanism
- [x] Start wipers
- [X] Brake car
- [x] Detect passenger weight
- [x] Turn on ambiental lights
- [x] Detect accident possibility 
- [X] Try to stop accident
- [X] Call family members in case of crash
- [ ] User can integrate 3rd party devices

See the [open issues](https://github.com/anacomo/KonnectedKars/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

## HTTP Connection

For the HTTP connection, we are using the [`Flask`](https://flask.palletsprojects.com/en/2.0.x/) library.

## Server API

The Server is exposing an API with a HTTP connection. 

Main routes of the API are:

* `/weight_sensor`
* `/speed_distance_sensor`
* `/crash_sensor`
* `/light_sensor`
* `/demisting_sensor`

<p align="right">(<a href="#top">back to top</a>)</p>

## MQTT Connection

### Server

We will use an online, free of charge MQTT broker: [Emqx Public Broker](https://www.emqx.com/en/mqtt/public-mqtt5-broker).

The server acts as the central main place for business logic.

For communication with othe sensors MQTT protocol is used, particularly package `paho-mqtt` from python

### Server Logic

The server is regularly trying to communicate with the seonsors by cheking the MQTT channels.

<p align="right">(<a href="#top">back to top</a>)</p>

## Unit testing
For unit testing we used the python library `unittest`. To run the tests, execute the commands:
```
python3 -m unittest unit-test
```

## Integration testing
This test works using the same `unittest` library and can be executed with `python3 -m unittest integration-test`. We wrote more comprehensive integration tests in the `integration-test.py` file. 

## Bug identification

As recommended, we used the Microsoft [Restler](https://github.com/microsoft/restler-fuzzer) tool with the following output

```
Starting task Test...
Using python: 'python3' (Python 3.10.2)
Request coverage (successful / total): 7 / 7
No bugs were found.
Task Test succeeded.
Collecting logs...
```


To reproduce, follow these stepts:

1. Install .NET 5.0 from [here](https://docs.microsoft.com/en-us/dotnet/core/install/linux?WT.mc_id=dotnet-35129-website)

2. Download the official repo
```sh
git clone https://github.com/microsoft/restler-fuzzer.git && cd restler-fuzzer
```

3. Create the folder for the Restler binaries
```sh
mkdir ../restler_bin
```

4. Build the Restler project
```sh
python3 ./build-restler.py --dest_dir ../restler_bin
```

5. Compile it
```sh
cd ../restler_bin
dotnet ./restler/Restler.dll compile --api_spec ../KonnectedKars/openapi.json
```

6. Run it
```sh
cd Compile
dotnet ./restler/Restler.dll test --grammar_file grammar.py --dictionary_file dict.json --settings engine_settings.json --no_ssl
```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Ciorica Vlad - vlad.ciorica@gmail.com

Project Link: [https://github.com/anacomo/KonnectedKars](https://github.com/anacomo/KonnectedKars)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Resources used:

* [Flask library](https://flask.palletsprojects.com/en/2.0.x/tutorial/)
* [paho-mqtt library](https://mqtt.org/)
* [free broker](https://www.emqx.com/en/mqtt/public-mqtt5-broker)
* [README Template](https://github.com/othneildrew/Best-README-Template)
* [Postman](https://www.postman.com/)
* [Twilio](https://www.twilio.com/login?g=%2Fconsole%2Fgate%3F&t=8b2a075839e7172cc38215f7b3e40bd6d82efda23afdc3fc0642e9b08271a400)
* [Microsoft RESTler](https://www.microsoft.com/en-us/research/publication/restler-stateful-rest-api-fuzzing/)
* [python unittest library]

Specs:
* OpenAPI Spec: [OpenAPI](../openapi.json)
* AsyncAPI Spec: [AsyncAPI](../asyncapi.yaml)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/anacomo/KonnectedKars/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/anacomo/KonnectedKars/network
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/anacomo/KonnectedKars/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/anacomo/KonnectedKars/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555