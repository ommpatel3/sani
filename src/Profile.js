import React, { Component } from 'react';
import {
  Person, userSession
} from 'blockstack';



export default class Profile extends Component {
  constructor(props) {
  	super(props);

  	this.state = {
  	  person: {
  	  	name() {
          return 'Anonymous';
        }
  	  },
  	};
  }

  render() {
    const { handleSignOut, userSession } = this.props;
    const { person } = this.state;
    return (
      !userSession.isSignInPending() ?
      <div>
        <div className="panel-welcome" id="section-2">
          <p className="lead">
            <button
              className="btn btn-primary btn-lg"
              id="signout-button"
              onClick={ handleSignOut.bind(this) }
            >
              Logout
            </button>
          </p>
        </div>
        <div id="table">
          <table>
            <tbody>
              <tr>
                <th>HEALTH CARD</th>
              </tr>
              <tr>
                <td></td>
                <th>Name</th>
                <td id="name"></td>
              </tr>
              <tr>
                <td><input type="checkbox"></input></td>
                <th>Healthcare ID</th>
                <td id="OHIPID"></td>
              </tr>
              {/* <tr>
                <td><input type="checkbox"></input></td>
                <th>Date of Birth</th>
                <td id="birth"></td>
              </tr> */}
            </tbody>
          </table>
        </div>
      </div> : null
    );
  }

  componentWillMount() {
    const { userSession } = this.props;
    this.setState({
      person: new Person(userSession.loadUserData().profile),
    });
      
  }
}


      var mqtt = require('mqtt');
      var client = mqtt.connect('broker',8883); //insert broker link
      
      client.subscribe('kismet');
      
      client.on('message', function (topic, message) {
        // message is Buffer
        /**
       * Converts an array buffer to a string
       *
       * @param {Uin8} uint8arr | The buffer to convert
       * @param {Function} callback | The function to call when conversion is complete
       */
        function largeuint8ArrToString(uint8arr, callback) {
          var bb = new Blob([uint8arr]);
          var f = new FileReader();
          f.onload = function(e) {
              callback(e.target.result);
        };
        
        f.readAsText(bb);
      }
      
      // Data in Uint8Array format
        var myuint8Arr = new Uint8Array(message);
      
        largeuint8ArrToString(myuint8Arr,function(text){
        // Data in english
          console.log(text);
          let c1 = text.indexOf('+');
          let name = text.slice(0,c1-1);
          let c2 = text.indexOf(',',c1+1);
          let ohip = text.slice(c1+1,c2-1);
          // let birth = text.slice(c2+1,-1)
      
          document.querySelector('#name').innerHTML = name;
          document.querySelector('#OHIPID').innerHTML = ohip;
          // document.querySelector('#birth').innerHTML = birth;
            
        });
        
        client.end();
      });