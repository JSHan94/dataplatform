pragma solidity ^0.6.6;

contract TradingPlatform{
    
    // token
    mapping (address => uint256) public balanceOf;
    event Buy(address _from,address _to, string _datah);
    event Balance(address user, uint balance);
    event Upload(string category, string name, string datahash, uint price);
    event GetData(uint timestamp, string category, string name, string datah, uint price, STATE state, address owner, address buyer);
    
    // data plaform
    enum STATE{ SALES, PROCESSING, SOLDOUT}
    
    struct Data{
        uint timestamp;
        string category;
        string name;
        string datahash;
        uint price;
        STATE state;
        address owner;
        address buyer;
    }
    
    mapping(string=>Data) data_list;
    
    Data newData;

    function giveToken(uint _token) public {
        balanceOf[msg.sender] += _token;
        
        emit Balance(msg.sender, balanceOf[msg.sender] );
    }
    
    function upload(string memory _category, string memory _name, string memory _datahash, uint _price) public{
        emit Upload(_category, _name, _datahash, _price);
        
        newData.timestamp = now;
        newData.category = _category;
        newData.name = _name;
        newData.datahash = _datahash; 
        newData.price = _price;
        newData.state = STATE.SALES;
        newData.owner = msg.sender;
        data_list[_datahash] = newData;
        
        
    }
    
    
    function buy(string memory _datahash) public payable {

        Data memory data = data_list[_datahash];
        /*
        require(data_list[_datah].owner != address(0)); //check exist Data
        require(balanceOf[msg.sender] >= data.price); // buyer has money
        require(data.owner != msg.sender ); // buyer != owner
        require(data.state == STATE.SALES); //data on sale
        require(data.buyer == address(0)); // no buyer yet
        */
        
        balanceOf[msg.sender] -= data.price; // buyer pay money
        balanceOf[data.owner] += data.price; // owner get money 
        emit Buy(data.owner,msg.sender,_datahash);
        
        
        //update data information
        data_list[_datahash].buyer = msg.sender;
        data_list[_datahash].state = STATE.PROCESSING;
        
    }
    
    function salesConfirm(string memory _datahash) public{
        
        require(data_list[_datahash].owner == msg.sender );
        require(data_list[_datahash].state == STATE.PROCESSING);
    
        data_list[_datahash].state = STATE.SOLDOUT;
        
    }
    
    
    function getData(string memory _datahash) public{
        Data memory data = data_list[_datahash];
        emit GetData(data.timestamp, data.category, data.name, data.datahash, data.price, data.state, data.owner, data.buyer);
    }
    
    
    
}

