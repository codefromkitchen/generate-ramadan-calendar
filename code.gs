// 1. Use https://www.extracttable.com/ to extract the table from https://www.muis.gov.sg/Ramadan-2022/Imsakiah
// 2. Paste in Google Sheet as is, delete blank rows if necessary, do not need to change any formatting
// 3. Run following script in Extensions > Apps Script 

function addIftarSahr() {
  var sheetSchedule = SpreadsheetApp.getActive().getSheetByName("Sheet1");
  // Caution! Always use getDisplayValues(), getValues() returns objects not strings (like Date/Number etc.)
  var data = sheetSchedule.getDataRange().getDisplayValues();
  for(var i = 1; i < data.length; i++) {
    var dateCol = data[i][8] .toString().split("/");
    var subhSadq = data[i][1].toString().split(" ");
    var maghrib = data[i][6].toString().split(" ");
    
    // Convert to UTC string to be used as param for Date() 
    // Reason: handling timezone issue in Date() is simply unmanageable.
    var start_time_sahr = dateCol[1] + '-' + dateCol[0] + '-' + dateCol[2] + ' ' 
                      + subhSadq[0] + ':' + (subhSadq[1] - 5) + ':' + '00 ' + 'UTC+8';
    var end_time_sahr = dateCol[1] + '-' + dateCol[0] + '-' + dateCol[2] + ' ' 
                      + subhSadq[0] + ':' + subhSadq[1] + ':' + '00 ' + 'UTC+8';
    var start_time_iftaar = dateCol[1] + '-' + dateCol[0] + '-' + dateCol[2] + ' ' 
                      + (parseInt(maghrib[0])+12) + ':' + (maghrib[1] - 5) + ':' + '00 ' + 'UTC+8';
    var end_time_iftaar = dateCol[1] + '-' + dateCol[0] + '-' + dateCol[2] + ' ' 
                      + (parseInt(maghrib[0])+12) + ':' + maghrib[1] + ':' + '00 ' + 'UTC+8';

    var event1 = CalendarApp.getDefaultCalendar().createEvent('Ramadan Notice: Today\'s Subah Sadiq ' + subhSadq[0] + ':' + subhSadq[1] + ' AM',
              new Date(start_time_sahr),
              new Date(end_time_sahr)
    );

    var event2 = CalendarApp.getDefaultCalendar().createEvent('Ramadan Notice: Today\'s iftaar ' + maghrib[0] + ':' + maghrib[1] + ' PM',
              new Date(start_time_iftaar),
              new Date(end_time_iftaar)
    );

    Logger.log("Sahr event created with ID: " + event1.getId());
    Logger.log("Iftaar event created with ID: " + event2.getId());
  }
}

function cleanUpAccidentalData() {
  // Be careful! never ever delete event without if..else. Even if you can undo it (probably), no telling if 
  // too many events are too much for Calendar app to recover.
  var events = CalendarApp.getDefaultCalendar().getEvents(new Date('April 25, 2022 00:00:00 UTC+8'), new Date('May 5, 2022 23:59:59 UTC+8'));
  Logger.log(events.length);
   for(var i = 0; i < events.length; i++){
     if(events[i].getTitle().startsWith("Ramadan Notice:")) { 
       Logger.log(events[i].getId()); 
      //  events[i].deleteEvent();
      }
   }
}
