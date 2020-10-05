from collections import deque
import pmdarima as pm

class WindowException(Exception) :
    pass

class SlidingWindow(deque) :
    def __init__(self, window_size) :
        super(SlidingWindow, self).__init__(maxlen = window_size)

    def is_full(self) :
        return len(self) == self.maxlen

class SlidingARIMA(SlidingWindow) :

    def __init__(self, window_size, seasonal = None) :
        self._seasonal = seasonal
        super(SlidingARIMA, self).__init__(window_size = window_size+1)
    
    def predict(self,forecast_horizon = 1) :
        if self.is_full() :
            try :
                if self._seasonal == None :
                    arima_fit = pm.auto_arima(
                        list(self)[1:self.maxlen - 1], start_p=1, start_q=1,
                        max_p=3, max_q=3, m=12,
                        start_P=0, seasonal=False,
               	        d=1, D=1, trace=False,
                        error_action='ignore', 
                        suppress_warnings=True,
                        stepwise=True)
                else :
                    arima_fit = pm.auto_arima(
                        list(self)[1:self.maxlen - 1], start_p=1, start_q=1,
                        max_p=3, max_q=3, m=12,
                        start_P=0, seasonal=True,
                        d=1, D=1, trace=False,
                        error_action='ignore', 
                        suppress_warnings=True,
                        stepwise=True)
                return float(arima_fit.predict(1)[0:forecast_horizon])
            except ValueError :
                print("Unable to estimate ARIMA. Lack of stationarity in differenced series")
                return(None)
        else : 
            return(None)