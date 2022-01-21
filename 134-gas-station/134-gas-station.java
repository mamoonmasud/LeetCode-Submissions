class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int sum_gas = 0;
        int sum_cost = 0;
        
        for (int i=0; i < gas.length; i++){
            sum_gas += gas[i];
                
        }
        for (int j=0; j < cost.length; j++){
            sum_cost += cost[j];
        }
        if (sum_gas - sum_cost < 0){
            return -1;
        }
        
        int gas_tank =0;
        int start_idx =0;
        
        for (int i =0; i < gas.length; i++){
            gas_tank += gas[i] - cost[i];
            if (gas_tank <0){
                start_idx = i+1;
                gas_tank= 0;
                    
            }
        }
        return start_idx;
        
        
    }
}




        