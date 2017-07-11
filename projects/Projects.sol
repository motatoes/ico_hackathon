
contract Projects {

  mapping(uint => Project) entries;
  uint public projectsCount = 0;

  struct Project {
      address clientAddress;
      string filehash;
      uint8 nvotes;
  }
  

  function create(string filehash) {
    Project storage entry = entries[projectsCount];
    entry.clientAddress = msg.sender;
    entry.filehash = filehash;
    entry.nvotes = 0;
    projectsCount++;


  }
  
  
  function get(uint8 i) constant returns (address clientAddress, string filehash, uint8 nvts) {
    Project entry = entries[i];
    return (
        entry.clientAddress,
        entry.filehash,
        entry.nvotes
    );
  }
  
  function getNumberOfProjects() constant returns(uint n) {
      return projectsCount;
  }  
  
  
  function addVote(uint8 i) {
      Project storage entry = entries[i];
      entry.nvotes = entry.nvotes + 1;
  }
  
  function getNumberOfVotes(uint8 i) constant returns(uint n) {
      Project storage entry = entries[i];
      return entry.nvotes;
  }    

}