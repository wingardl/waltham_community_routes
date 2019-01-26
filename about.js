'use strict';

constant about_page = React.createElement;

class AboutPage extends React.Component{
  render() {
    return (
      <header> About WPY </header>
    );
  }
}

const domContainer = document.querySelector('#about_page');
ReactDOM.render(about_page(AboutPage), domContainer);
